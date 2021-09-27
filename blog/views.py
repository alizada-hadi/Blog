from django.db import models
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Blog, Comment
from .forms import BlogForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Like
from django.views import generic

from django.views.generic.edit import FormMixin


class PostListView(generic.ListView):
    queryset = Blog.objects.filter(status='published')
    template_name = "blog/index.html"
    context_object_name = "blogs"


class PostDetailView(FormMixin, generic.DetailView):
    model = Blog
    template_name = "blog/post_detail.html"
    form_class = CommentForm

    def get_success_url(self):
        return reverse("post-detail", kwargs={"slug": self.object.slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid()

    def form_valid(self, form):
        form.instance.post = self.object
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)


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


def like_post(request):
    user = request.user

    if request.method == "POST":
        post_id = request.POST.get('post_id')
        post_obj = Blog.objects.get(id=post_id)
        if user in post_obj.likes.all():
            post_obj.likes.remove(user)
        else:
            post_obj.likes.add(user)

        like, created = Like.objects.get_or_create(user=user, post_id=post_id)
        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        like.save()
    return redirect('post-list')


class CreateComment(LoginRequiredMixin,  generic.CreateView):
    template_name = "blog/post_detail.html"

    model = Comment
    fields = [
        'post',
        'comment'
    ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
