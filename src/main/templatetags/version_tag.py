import os
from django import template

register = template.Library()


@register.simple_tag
def image_version():
    return os.getenv('APP_VERSION')
