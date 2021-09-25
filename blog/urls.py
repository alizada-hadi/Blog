from django.urls import path

from . import views
urlpatterns = [
    path("", views.PostListView.as_view(), name="post-list"),
    path("blog/<slug:slug>/",
         views.PostDetailView.as_view(), name="post-detail"),
    path("create/", views.PostCreateView.as_view(), name="post-create"),
    path("blog/<slug:slug>/update/",
         views.PostUpdateView.as_view(), name="post-update"),
    path("blog/<slug:slug>/delete/",
         views.BlogDeleteView.as_view(), name="post-delete"),

    path("like/", views.like_post, name="like-post")

]
