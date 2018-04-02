#!/usr/bin/env bash
# sets up web servers for deployment of web_static
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p data/web_static/releases/test data/web_static/shared
sudo touch data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
sudo sed -i '37i\
\
\tlocation /hbnb_static/ {\
\talias /data/web_static/current/;\
\t}' /etc/nginx/sites-available/default
sudo service nginx start
