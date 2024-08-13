from django import template

register = template.Library()


@register.filter
def blog_media_filter(path):
    if path:
        return f'/media/{path}'
    return "/media/catalog/image/LG.jpg"
