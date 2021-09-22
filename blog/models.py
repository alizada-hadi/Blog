from django.db import models
from django.utils import timezone


class Blog(models.Model):
    # owner =
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="blogs/images/", null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-title']

    def __str__(self):
        return self.title
