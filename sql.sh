mysql -uroot -e "create database db1"
mysql -uroot -e "create user 'django'@'localhost' identified by '123'"
mysql -uroot -e "grant all on db1.* to 'django'@'localhost'"
