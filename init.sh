#!/bin/bash

# sudo apt-get update
# sudo apt-get -y install nginx
# sudo pip install --upgrade pip
# sudo pip install gunicorn django

# links config files
sudo rm -rf /etc/nginx/sites-enabled/*
sudo rm -rf /etc/gunicorn.d/*
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/vservers.conf
sudo ln -s /home/box/web/etc/hello.py    /etc/gunicorn.d/hello.py

# test nginx  configs
sudo nginx -t
# start nginx service
sudo /etc/init.d/nginx start
# graceful restart
NGINX_MASTER_PID=`ps aux |grep 'nginx: master' | head -1 | awk '{print $2}'`
sudo kill -HUP $NGINX_MASTER_PID

# start application server
cd ask
gunicorn ask.wsgi:application --bind 0.0.0.0:8000 --workers=5
