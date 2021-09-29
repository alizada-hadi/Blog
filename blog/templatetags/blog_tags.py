from django import template
from ..models import Blog
register = template.Library()


def total_posts():
    return Blog.objects.count()
