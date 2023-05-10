from django import template
from django.utils.safestring import mark_safe
import markdown

register = template.Library()

@register.filter
def sub(value, arg):
    return value - arg
# value = lists.paginator.count
# arg = lists.start_index


# markdown라이브러리 설치 후 함수 사용 선언..
@register.filter
def mark(value):
    extensions = ["nl2br", "fenced_code"]
    return mark_safe(markdown.markdown(value, extensions=extensions))