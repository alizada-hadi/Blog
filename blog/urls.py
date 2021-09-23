from django.urls import path

from . import views
urlpatterns = [
    path("", views.index, name="index-page"),
    path("post/<int:pk>/", views.post_detail, name="post-detail"),
    path("create/", views.create_post, name="create-blog"),
    path("post/update/<int:pk>/", views.post_update, name="post-update"),
]
