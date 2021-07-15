from django.template import Library

register = Library()


@register.simple_tag
def get_lang_url(url, lang):
    url = url.split('/')
    url[1] = lang
    return '/'.join(url)
