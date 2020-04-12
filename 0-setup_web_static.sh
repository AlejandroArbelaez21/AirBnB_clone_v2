#!/usr/bin/env bash
#This Bash script sets up your web servers for the deployment of web_static
sudo apt-get update
sudo apt-get install nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
if [ -h /data/web_static/current ]
then
  unlink /data/web_static/current
  ln -s /data/web_static/releases/test /data/web_static/current
else
  ln -s /data/web_static/releases/test /data/web_static/current
fi
chown -R ubuntu:ubuntu /data/
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx restart
