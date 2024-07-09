from django import template

register = template.Library()

@register.filter
def truncate_words(value, arg):
    words = value.split()[:arg]
    return ' '.join(words) + (' ...' if len(words) < len(value.split()) else '')
