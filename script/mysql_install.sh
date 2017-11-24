#!/usr/bin/env bash
#полезные команды
#УСТАНОВКА
#sudo apt-get install mysql-server
#НАСТРОЙКА удаленного подключения к MySql
#sudo cat /etc/mysql/mysql.conf.d/mysqld.cnf | sed 's/^#?bind-address.*$ 0.0.0.0/bind-address		= 0.0.0.0/g'
#sudo /etc/init.d/mysql restart
#настраиваем права для удаленного подключения
#sudo mysql -u root -p
#GRANT ALL PRIVILEGES ON *.* TO root@'%' IDENTIFIED BY 'Gh84mcsajkn';
GRANT ALL PRIVILEGES ON *.* TO root@'%' IDENTIFIED BY '1';


#команды для lesson 5
sudo /etc/init.d/mysql start
mysql -u root -e "CREATE DATABASE  IF NOT EXISTS `sitedb`"
