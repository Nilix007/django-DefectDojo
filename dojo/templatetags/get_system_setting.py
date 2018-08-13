from django import template
from dojo import utils

register = template.Library()


@register.filter
def get_system_setting(system_setting):
    try:
        setting = utils.get_system_setting(system_setting)
        if setting:
            return setting
        else:
            return False
    except Exception as e:
        return False
