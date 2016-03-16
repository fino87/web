sudo rm /etc/nginx/sites-available/default
sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/nginx.conf
sudo ln -s /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo /etc/init.d/nginx restart
sudo gunicorn -c /etc/gunicorn.d/hello.py hello:wsgi_application
sudo gunicorn --bind 0.0.0.0:8000 --access-logfile acc.log --error-logfile err.log ask.wsgi:application
