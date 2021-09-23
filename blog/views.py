from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Blog
from .forms import BlogForm
from django.contrib.auth.decorators import login_required


def index(request):
    blogs = Blog.objects.all()
    context = {
        "title": "Index",
        "blogs": blogs
    }
    return render(request, "blog/index.html", context)


@login_required
def create_post(request):
    user = request.user
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        Blog.objects.create(owner=user, title=title,
                            content=content, image=image)
    return render(request, "blog/create_post.html")


def post_detail(request, pk):
    post = Blog.objects.get(pk=pk)
    context = {
        "post": post
    }
    return render(request, 'blog/post_detail.html', context)


def post_update(request, pk):
    obj = Blog.objects.get(pk=pk)

    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=obj)
        if form.is_valid:
            form.save()
    else:
        form = BlogForm()

    return render(request, "blog/post_update.html", {"form": form})
