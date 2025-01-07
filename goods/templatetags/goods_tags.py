from django import template
from goods.models import Categorys
import datetime
from django.utils.http import urlencode

register=template.Library()

@register.simple_tag()
def tag_categorys():
    return Categorys.objects.all()

@register.simple_tag()
def current_time():
    return datetime.datetime.now()

@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context["request"].GET.dict()
    query.update(kwargs)
    return urlencode(query)