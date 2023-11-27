from django import template
from datetime import datetime


register = template.Library()


@register.simple_tag()
def updated():
    current_date_time = datetime.now()
    return current_date_time.strftime('%d.%m.%Y %H:%M:%S')
