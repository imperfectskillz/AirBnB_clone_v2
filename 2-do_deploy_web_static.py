#!/usr/bin/python3
#fabric script generates a tgz archive
from fabric.api import *
from datetime import datetime
import os


env.hosts = ["52.91.246.129", "107.23.155.217"]


def do_pack():
    """
    creates tgz
    """
    filetime = datetime.now().strftime('%Y%m%d%H%M%s')
    filename = 'versions/web_static_{}.tgz'.format(filetime)
    try:
        local("mkdir -p versions")
        local('tar -cvzf {} web_static'.format(filename))
        return filename
    except:
        return None


def do_deploy(archive_path):
    """
    distributes archive to web servers
    """
    file = archive_path.split("/")[1]

    if os.path.exists(archive_path):
        put(archive_path, "/tmp/")
        file1 = file.split(".")[0]
        run("mkdir -p /data/web_static/releases/{}/".format(file1))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(file, file1))
        run("rm /tmp/{}".format(file))
        run("cp /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(file1, file1))
        run("rm -rf /data/web_static/releases/{}/web_static".format(file1))
        run("rm /data/web_static/current")
        run("ln -sf /data/web_static/releases/{}/ /data/web_static/current".format(file1))
        return True

    return False
