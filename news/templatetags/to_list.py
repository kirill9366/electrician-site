from django import template

register = template.Library()


@register.filter
def to_list(value):
    return list(map(lambda x: int(x), value.split()))
