from django.template import Library

register = Library()


# @register.filter
# def cut(text, n):
#     return text[:n]


# def upper(txt):
#     return txt.upper()  # txt[0]
@register.simple_tag
def cut_string(txt, n):
    return txt[:n]
