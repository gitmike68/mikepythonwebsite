#!/usr/bin/env bash

#для Python 2
cd /home/box/web/ask
sudo python3 manage.py makemigrations qa
#sudo python3 manage.py sqlmigrate qa 0006
sudo python3 manage.py migrate
