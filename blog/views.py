from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog


def index(request):
    blogs = Blog.objects.all()
    context = {
        "title": "Index",
        "blogs": blogs
    }
    return render(request, "blog/index.html", context)
