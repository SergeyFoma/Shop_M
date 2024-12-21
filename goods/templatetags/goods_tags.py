from django import template
from goods.models import Categorys

register=template.Library()

@register.simple_tag()
def tag_categorys():
    return Categorys.objects.all()