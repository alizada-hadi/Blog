from django.contrib import admin
from .models import Blog, Comment


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'created', 'updated', )
    list_filter = ('title', 'body', )
    search_fields = ('title',  'body',)


admin.site.register(Comment)
