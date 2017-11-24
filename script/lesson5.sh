#!/usr/bin/env bash
#запускаем mysql и делаем БД
sudo /etc/init.d/mysql start
mysql -u root -e "CREATE DATABASE  IF NOT EXISTS `sitedb`;"
#запускаем приложение Django
cd /home/box/web/ask/
sudo gunicorn ask.wsgi -c /home/box/web/etc/ask.py