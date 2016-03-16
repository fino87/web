mysql -uroot -e "create database webdb"
mysql -uroot -e "create user 'fino'@'localhost' identified by '123'"
mysql -uroot -e "grant all on webdb.* to 'fino'@'localhost'"
