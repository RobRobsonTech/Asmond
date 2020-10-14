#!/bin/bash

echo "Start Network Scan"
ip_address=$(python ~/Documents/1-New-ND-Git/network-defender/scripts/getIP.py)

#nmap2db.pl --db db.sqlite3 --table networkdefender_nmapscan --scan 192.168.1.72

#$ip_address
#nmap2db.pl [--db ~/Documents/1-New-ND-Git/network-defender/networkMapper/db.sqlite3][--table networkdefender_nmapscan] --scan $ip_address-255

#nmap2sqlite.pl [--db ~/Documents/1-New-ND-Git/network-defender/networkMapper/db.sqlite3][--table networkdefender_nmapscan] --scan $ip_address-1
#nmap2sqlite.pl [--db ~/Documents/1-New-ND-Git/network-defender/networkMapper/db.sqlite3][--table networkdefender_nmapscan] --scan $ip_address-255

#nmap -sS -A -F -oX outputfile.xml $ip_address-1
#nmap -sS -A -F -oX outputfile.xml $ip_address-255

#nmap -sS -A -F --script sqlite-output --script-args=dbname="~/Documents/1-New-ND-Git/network-defender/networkMapper/db.sqlite3",dbtable=nmapscan 192.168.1.1-254

#nmap -sS -A -F --script sqlite-output --script-args=dbname="~/Documents/1-New-ND-Git/network-defender/networkMapper/db.sqlite3",dbtable=nmapscan scanme.nmap.org
#sqlite3 db.sqlite3

#nmap2db.pl --dbtype sqlite --dbname db
