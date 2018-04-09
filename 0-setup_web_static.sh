#!/usr/bin/env bash
# prepares web servers
sudo apt-get update
sudo apt-get install nginx -y
sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/
sudo echo -e "James CHoi" >> /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i "38i \tlocation /hbnb_static {\n\talias /data/web_static/current;\n\t}" /etc/nginx/sites-available/default
sudo service nginx restart
