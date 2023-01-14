#!/bin/bash

echo "Устонавливаем программу. Пожалуйста подождите, это может занять некоторое времья!"
cp -r install/wifi_deauth /usr/sbin/

apt install -y gnome-terminal
pip install colorama

mkdir /prog 
mkdir /prog/Wifi_deauth/
cp -r install/setup.py /prog/Wifi_deauth/

echo "Установка была завершена для запуска программы пропишите команду wifi_deauth"
