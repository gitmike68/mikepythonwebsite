#!/usr/bin/env bash

#для Python 2
cd /home/box/web/ask
sudo python manage.py makemigrations qa
#sudo python manage.py sqlmigrate qa 0006
sudo python manage.py migrate
