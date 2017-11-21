#!/usr/bin/env bash
sudo rm /etc/gunicorn.d/hello.py
sudo ln -s /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo /etc/init.d/nginx restart
sudo gunicorn -c /etc/gunicorn.d/hello.py /home/box/web/hello.py