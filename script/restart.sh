#!/usr/bin/env bash
sudo /etc/init.d/nginx restart
cd /home/box/web/ask/
sudo gunicorn ask.wsgi -c /home/box/web/etc/ask.py