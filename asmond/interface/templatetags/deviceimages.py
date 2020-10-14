from django import template

register = template.Library()


@register.filter(name='make_device_path')
def make_device_path(device):
    """
    Gets tenant and tenant parent to assist in the choosing of logo
    :param device_type: Device type
    :return: The user's tenant's logo
    """

    device_image_path = "framework\\img\\devices\\" + device.device_type + ".png"

    return {
        "device_image_path": device_image_path
    }
