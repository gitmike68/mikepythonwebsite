#!/usr/bin/env bash
#cd /home/box/web/
#sudo gunicorn -c /etc/gunicorn.d/hello.py hello
cd /home/box/web/ask/
sudo gunicorn ask.wsgi -c /home/box/web/etc/ask.py