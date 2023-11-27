from django import template
import requests


register = template.Library()


@register.simple_tag(takes_context=True)
def exchange(context, money):
    response = requests.get('https://v6.exchangerate-api.com/v6/bb1cc5a13cc79aade21b246b/latest/USD')
    data = response.json()
    exchanged_money = money * data["conversion_rates"][currency]
    return f"{exchanged_money:.2f} {currency}"
