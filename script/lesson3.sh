#!/usr/bin/env bash
sudo rm /etc/gunicorn.d/hello.py
sudo rm -r /etc/gunicorn.d
sudo mkdir /etc/gunicorn.d
sudo ln -s /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
cd /home/box/web/
#sudo gunicorn -c /etc/gunicorn.d/hello.py hello
cd /home/box/web/ask/
sudo gunicorn ask.wsgi -c /home/box/web/etc/ask.py