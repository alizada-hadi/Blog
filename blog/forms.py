from django import forms
from django.db.models import fields
from .models import Blog, Comment


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
