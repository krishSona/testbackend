import payout
from django import template

register = template.Library()


@register.simple_tag
def get_balance():
    return payout.get_balance()
