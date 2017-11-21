#!/usr/bin/env bash
sudo rm /etc/gunicorn.d/hello.py
sudo ln -s /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo cd /home/box/web/
sudo gunicorn -c /etc/gunicorn.d/hello.py hello