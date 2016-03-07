sudo rm /etc/nginx/sites-available/default
sudo rm /etc/nginx/sites-enabled/default
sudo ﻿ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/nginx.conf
sudo /etc/init.d/nginx restart
