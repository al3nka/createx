from django import template

register = template.Library()


@register.simple_tag
def generate_list_view_link(**kwargs):
    return f"?{ '&'.join(f'{k}={v}' for k, v in kwargs.items() if v) }"
