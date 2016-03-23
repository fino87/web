sudo mysqld_safe &
sleep 5
sudo mysql -uroot -e "create database myproject;"
sudo mysql -uroot -e "CREATE USER 'slobanov'@'localhost' IDENTIFIED BY 'password';"
sudo mysql -uroot -e "GRANT ALL PRIVILEGES ON * . * TO 'slobanov'@'localhost';"
sudo mysql -uroot -e "FLUSH PRIVILEGES;"
sudo ../ask/manage.py syncdb
sudo cp /home/box/web/etc/nginx.conf  /etc/nginx/nginx.conf
sudo /etc/init.d/nginx restart
cd ../ask
sudo gunicorn -b 0.0.0.0:8000 ask.wsgi
