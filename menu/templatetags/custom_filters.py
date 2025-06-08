from django import template
from django.forms import BoundField

register = template.Library()

@register.filter
def add_class(field, css_class):
    if isinstance(field, BoundField):
        return field.as_widget(attrs={"class": f"{css_class} {field.css_classes() if field.css_classes() else ''}"})
    return field