The following commands will need to be used in order to make the shell scripts
runnable and begin on startup:

1) Visit root/etc/local.rc file and add your scripts in
(use & symbol to make them run in the background)
sudo nano /etc/rc.local

2) Make your scripts runnable: (can run without the u)
chmod u+x ~/Documents/1-New-ND-Git/network-defender/scripts/startup.sh
chmod u+x ~/Documents/1-New-ND-Git/network-defender/scripts/nmap-scan.sh

3) crontab in etc - At the bottom add:
@reboot ~/Documents/1-New-ND-Git/network-defender/scripts/startup.sh
@reboot ~/Documents/1-New-ND-Git/network-defender/scripts/nmap-scan.sh
crontab -e

4) git reset --hard

