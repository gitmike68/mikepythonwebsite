#!/usr/bin/env bash
sudo rm /etc/gunicorn.d/hello.py
sudo ln -s /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo rm -r /etc/gunicorn.d
sudo mkdir /etc/gunicorn.d
cd /home/box/web/
sudo gunicorn -c /etc/gunicorn.d/hello.py hello