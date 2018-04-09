#!/usr/bin/python3
# fabric script generates a tgz archive
from fabric.api import *
from datetime import datetime


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
