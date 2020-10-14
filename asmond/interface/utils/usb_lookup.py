import re
import subprocess
import os

try:
    import win32api
    import win32file
    print("Windows API loaded successfully")
except ImportError:
    print("Unable to load Windows API")


def linux_usb():
    print("Checking USBs: ")
    small_usb = False
    midsize_usb = False
    large_usb = False
    enterprise_usb = False

    # Mount Small USB
    try:
        os.system("mount /media/1-SMALL")
    except:
        print("no small usb")

    # Mount Midsize USB
    try:
        os.system("mount /media/2-MIDSIZE")
    except:
        print("no midsize usb")

    # Mount Large USB
    try:
        os.system("mount /media/3-LARGE")
    except:
        print("no large usb")

    # Mount Enterprise USB
    try:
        os.system("mount /media/4ENTERPRISE")
    except:
        print("no enterprise usb")

    # Small USB
    if os.path.ismount('/media/1-SMALL') == True:
        small_usb = True
        print("Small USB Connected")
    # Midsize USB
    if os.path.ismount('/media/2-MIDSIZE') == True:
        midsize_usb = True
        print("Midsize USB Connected")
    # Large USB
    if os.path.ismount('/media/3-LARGE') == True:
        large_usb = True
        print("Large USB Connected")
    # Enterprise USB
    if os.path.ismount('/media/4ENTERPRISE') == True:
        enterprise_usb = True
        print("Enterprise USB Connected")
    # No USBs Connected
    if (os.path.ismount('/media/1-SMALL') == False) & (os.path.isdir('/media/2-MIDSIZE') == False) & (os.path.isdir('/media/3-LARGE') == False) & (os.path.isdir('/media/4ENTERPRISE') == False):
        print("No USB devices connected!")

    return small_usb, midsize_usb, large_usb, enterprise_usb


def win_usb():
    print("Checking USB Devices...")
    small_usb = False
    midsize_usb = False
    large_usb = False
    enterprise_usb = False
    drive_names = []

    # Returns a list containing letters from removable drives
    drive_list = win32api.GetLogicalDriveStrings()
    drive_list = drive_list.split("\x00")[0:-1]  # the last element is ""
    for letter in drive_list:
        if win32file.GetDriveType(letter) == win32file.DRIVE_REMOVABLE:  # check if the drive is of type removable
            print("list drives: {0}".format(letter))
            # If drive name == small_usb
            # set small_usb to True
            full_info = win32api.GetVolumeInformation(letter)
            current_drive = full_info[0]
            drive_names.append(current_drive)

    for usb_name in drive_names:
        if usb_name == "1-SMALL":
            small_usb = True
            print("Small USB Connected")
        elif usb_name == "2-MIDSIZE":
            midsize_usb = True
            print("Midsize USB Connected")
        elif usb_name == "3-LARGE":
            large_usb = True
            print("Large USB Connected")
        elif usb_name == "4ENTERPRISE":
            enterprise_usb = True
            print("Enterprise USB Connected")
    if not drive_names:
        print("No USB devices connected!")

    return small_usb, midsize_usb, large_usb, enterprise_usb



