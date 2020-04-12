#!/usr/bin/env bash
#This Bash script sets up your web servers for the deployment of web_static
sudo apt-get update
sudo apt-get install nginx
if [ -d /data/ ];
then
  :
else
  sudo mkdir /data
fi
if [ -d /data/web_static ];
then
  :
else
  sudo mkdir /data/web_static/
fi
if [ -d /data/web_static/releases ];
then
  :
else
  sudo mkdir /data/web_static/releases
fi
if [ -d /data/web_static/shared ];
then
  :
else
  sudo mkdir /data/web_static/shared
fi
if [ -d /data/web_static/releases/test ];
then
  :
else
  sudo mkdir /data/web_static/releases/test
fi
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
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx restart
