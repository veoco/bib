from django import template
from django.utils.safestring import mark_safe

from misaka import Markdown, SaferHtmlRenderer


register = template.Library()

rndr = SaferHtmlRenderer()
md = Markdown(rndr)


@register.filter()
def markdown(content):
    result = md(content)
    return mark_safe(result)


@register.filter()
def text_more(content):
    content = content.split('\n')[0]
    return content
