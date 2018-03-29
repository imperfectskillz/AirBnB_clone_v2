#!/usr/bin/bash env
# prepares web servers
sudo apt-get update
sudo apg-get install nginx
mkdir /data/
mkdir /data/web_static/
mkdir /data/web_static/releases/
mkdir /data/web_static/shared/
mkdir /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html
echo "James CHoi" >> /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data
sed -i "39i \tlocation /hbnb_static {\n\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-enabled/default
service nginx restart
