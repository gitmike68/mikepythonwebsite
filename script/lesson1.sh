#!/usr/bin/env bash
sudo rm -r /home/box
sudo rm /etc/nginx/sites-enabled/test.conf
sudo git clone https://github.com/gitmike68/mikepythonwebsite /home/box/
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart