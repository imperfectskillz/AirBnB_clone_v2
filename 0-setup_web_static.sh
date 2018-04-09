#!/usr/bin/env bash
# prepares web servers
sudo apt-get update
sudo apt-get install nginx -y
sudo mkdir /data/
sudo mkdir /data/web_static/
sudo mkdir /data/web_static/releases/
sudo mkdir /data/web_static/shared/
sudo mkdir /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
sudo echo -e "James CHoi" >> /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
sudo sed -i "39i \tlocation /hbnb_static {\n\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-enabled/default
sudo service nginx restart
