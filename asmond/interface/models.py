from django.db import models

# Asmond Databases Listed Here


class NetworkDevices(models.Model):
    """
    Store journey time alert configuration
    """
    device_type = models.TextField(blank=True, verbose_name="Device Type", default=None, null=True)

    hostname = models.TextField(blank=True, default=None, verbose_name="Hostname")

    ip_address = models.TextField(blank=True, default=None, verbose_name="IP Address")

    mac_vendor = models.TextField(blank=True, default=None, verbose_name="MAC Vendor", null=True)

    device_level = models.IntegerField(default=1, verbose_name="Device Level")

    connects_to = models.TextField(blank=True, default=None, verbose_name="Connects To", null=True)


class NetworkOverview(models.Model):
    """
    Store number of certain devices
    """
    device_type = models.TextField(blank=True, verbose_name="Device Type", default=None, null=True)

    number_of_devices = models.IntegerField(default=1, verbose_name="Number Of Devices")


class NetworkProblems(models.Model):
    """
    Store problems found for each device
    """
    device = models.ForeignKey("interface.NetworkDevices", null=True, default=None, verbose_name="Devices", db_index=True, on_delete=models.CASCADE)

    device_problem = models.TextField(default=None, verbose_name="Device Problem")

    problem_severity = models.IntegerField(default=0, verbose_name="Problem Severity")


class NmapScan(models.Model):
    """
    Store journey time alert configuration
    """
    hostname = models.TextField(blank=True, default=None, verbose_name="Hostname")

    ip_address = models.TextField(blank=True, default=None, verbose_name="IP Address")

    port_number = models.IntegerField(default=0, null=True, verbose_name="Port Number")

    protocol_type = models.TextField(blank=True, default=None, verbose_name="Protocol Type (TCP/UDP)")

    device_state = models.TextField(blank=True, default=None, verbose_name="Device State")

    device_service = models.TextField(blank=True, default=None, verbose_name="Device Service")

    device_version = models.TextField(blank=True, default=None, verbose_name="Device Version")
