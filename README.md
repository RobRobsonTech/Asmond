# network-mapper
First copy latest copy over of code

Step 1) ifconfig on raspberry pi
Step 2) Putty into the raspberry pi via laptop
Step 3) CD to Asmond V2
Step 4) Load server: python3 manage.py runserver IP:8000
Step 5) Load Website: IP:8000/networkdefender

Bonus) Kill All Port 8000: sudo fuser -k 8000/tcp

Install Requirements:
pip install -r requirements.txt