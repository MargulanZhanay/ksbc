from django import template

register = template.Library()


@register.filter
def addclass(field, css):
    return field.as_widget(attrs={'class': css})


@register.filter
def add_active_class(url, current_url):
    return 'active' if url == current_url else ''
