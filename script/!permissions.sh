#!/usr/bin/env bash
sudo chown -R mike:mike /home
cd /home/
#меняем владельца
sudo chown -R mike:mike /home/box
#меняем права
sudo chmod 777 box
sudo chmod 777 box/*/*
sudo chmod 777 box/*/*/*
sudo chmod 777 box/*/*/*/*
sudo chmod 777 box/*/*/*/*/*