# templatetags/filters.py
from django import template
from django.utils.html import format_html
from django.contrib.sites.models import Site

register = template.Library()

@register.filter
def absolute_url(value):
    domain = Site.objects.get_current().domain
    return format_html('https://{}{}'.format(domain, value))
