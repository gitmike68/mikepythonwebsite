#!/usr/bin/env bash
cd /home
#меняем владельца
sudo chown -R mike:mike /home/box
#меняем права
sudo chmod 777 box
sudo chmod 777 box/*/*
sudo chmod 777 box/*/*/*
sudo chmod 777 box/*/*/*/*
sudo chmod 777 box/*/*/*/*/*