#!/bin/bash

echo "cd to network mapper directory"
cd ~/Documents/1-New-ND-Git/network-defender/networkMapper/

echo "flush database"
python ~/Documents/1-New-ND-Git/network-defender/networkMapper/manage.py flush --no-input
sleep 5

echo "python start app"
ip_address=$(python ~/Documents/1-New-ND-Git/network-defender/scripts/getIP.py)
echo "Found IP: $ip_address"
python ~/Documents/1-New-ND-Git/network-defender/networkMapper/manage.py runserver $ip_address:8000 &
sleep 5

echo "Start Browser Sensibly"
sleep 5
sensible-browser http://$ip_address:8000/ &

firefox &

echo "Start Browser Attempt 1"
xdg-open http://$ip_address/

echo "Start Browser Attempt 2"
python -m webbrowser -t "http://$ip_address/"

echo "Start Browser Attempt 3"
firefox http://$ip_address/
sleep 5

echo "Full Screen"
xdotool key F11

/usr/bin/firefox http://$ip_address/
sleep 1
xdotool key F11