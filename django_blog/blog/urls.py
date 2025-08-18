from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView,
    BlogLoginView, BlogLogoutView, register, profile
)

urlpatterns = [
    path("login/",  BlogLoginView.as_view(),  name="login"),
    path("logout/", BlogLogoutView.as_view(), name="logout"),
    path("register/", register,               name="register"),
    path("profile/",  profile,                name="profile"),

    path("posts/", PostListView.as_view(), name="post-list"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),  # singular "post"
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),  # use "update"
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
]
