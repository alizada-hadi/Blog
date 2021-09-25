from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify

import string
import random

from django.urls import reverse


def random_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))


class Blog(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(User,
                               related_name='blog_posts',  on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='blog/images/', null=True, blank=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')

    likes = models.ManyToManyField(User, default=None, blank=True)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(random_slug() + "-" + self.title)
        super(Blog, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug': self.slug})

    @property
    def number_of_likes(self):
        return self.likes.count()


LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike')
)


class Like(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES,
                             default='Unlike', max_length=20)

    def __str__(self):
        return 'f{self.user}\'s like'
