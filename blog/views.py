from django.db import models
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Blog
from .forms import BlogForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


from django.views import generic


class PostListView(generic.ListView):
    queryset = Blog.objects.filter(status='published')
    template_name = "blog/index.html"
    context_object_name = "blogs"


class PostDetailView(generic.DetailView):
    model = Blog
    template_name = "blog/post_detail.html"


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "blog/create_post.html"
    model = Blog
    fields = [
        'title',
        'image',
        'body',
        'status'
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    template_name = "blog/post_update.html"
    model = Blog
    fields = [
        'title',
        'image',
        'body',
        'status'
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        blog = self.get_object()
        if self.request.user == blog.author:
            return True
        return False


class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Blog
    success_url = '/'

    def test_func(self):
        blog = self.get_object()
        if self.request.user == blog.author:
            return True
        return False
