#!/usr/bin/env bash
cd /
sudo rm -r /home/box
sudo rm /etc/nginx/sites-enabled/test.conf
#sudo git clone https://github.com/gitmike68/mikepythonwebsite /home/box/
#sudo git clone -b lesson2 https://github.com/gitmike68/mikepythonwebsite /home/box/
sudo git clone -b lesson4 https://github.com/gitmike68/mikepythonwebsite /home/box/
#
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
#sudo bash /home/box/script/lesson4.sh