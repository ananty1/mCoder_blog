from django import template

register = template.Library()

@register.filter(name ='get_vals')

def get_vals(dict,key):
    return dict.get(key)
