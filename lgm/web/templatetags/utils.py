from django import template

register = template.Library()


@register.filter
def index(l, i):
    return l[int(i)]


@register.filter(name='range')
def range_(i):
    return range(int(i))
