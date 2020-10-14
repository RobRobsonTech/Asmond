import subprocess, os

from django.db.models.functions import Lower, Upper
from django.shortcuts import render
from .models import NetworkOverview, NetworkDevices, NetworkProblems, NmapScan
from .utils.usb_lookup import win_usb, linux_usb


def homepage(request):
    devices_overview = NetworkOverview.objects.all()
    devices_found = NetworkDevices.objects.all()
    device_problems = NetworkProblems.objects.all()

    device_problems = device_problems.order_by(Lower("problem_severity"))

    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_address = s.getsockname()[0]

    # If small USB is connected
    # Set small usb to True
    # Else set small usb to False

    if os.name == 'nt':
        print("OS: Windows")
        usb_sizes = win_usb()
    else:
        print("OS: Linux/Other")
        usb_sizes = linux_usb()

    small_usb = usb_sizes[0]
    midsize_usb = usb_sizes[1]
    large_usb = usb_sizes[2]
    enterprise_usb = usb_sizes[3]

    return render(request, "interface/homepage.html", {
        "devices_overview": devices_overview,
        "devices_found": devices_found,
        "device_problems": device_problems,
        "ip_address": ip_address,
        "small_usb": small_usb,
        "midsize_usb": midsize_usb,
        "large_usb": large_usb,
        "enterprise_usb": enterprise_usb
    })


def networkmap(request):
    devices_overview = NetworkOverview.objects.all()
    devices_found = NetworkDevices.objects.all()
    device_problems = NetworkProblems.objects.all()
    nmap_device = NmapScan.objects.all()

    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_address = s.getsockname()[0]

    return render(request, "interface/networkmap.html", {
        "devices_overview": devices_overview,
        "devices_found": devices_found,
        "device_problems": device_problems,
        "nmap_device": nmap_device,
        "ip_address": ip_address
    })


def networkdevices(request):
    devices_overview = NetworkOverview.objects.all()
    devices_found = NetworkDevices.objects.all()
    device_problems = NetworkProblems.objects.all()
    nmap_device = NmapScan.objects.all()

    return render(request, "interface/networkdevices.html", {
        "devices_overview": devices_overview,
        "devices_found": devices_found,
        "device_problems": device_problems,
        "nmap_device": nmap_device
    })


def networkproblems(request):
    devices_overview = NetworkOverview.objects.all()
    devices_found = NetworkDevices.objects.all()
    device_problems = NetworkProblems.objects.all()

    device_problems = device_problems.order_by(Lower("problem_severity"))

    #subprocess.call(['./problems.sh'])

    return render(request, "interface/networkproblems.html", {
        "devices_overview": devices_overview,
        "devices_found": devices_found,
        "device_problems": device_problems
    })
