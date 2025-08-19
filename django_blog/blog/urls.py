from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView,
    BlogLoginView, BlogLogoutView, register, profile
)
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView
from . import views


urlpatterns = [
    path("login/",  BlogLoginView.as_view(),  name="login"),
    path("logout/", BlogLogoutView.as_view(), name="logout"),
    path("register/", register,               name="register"),
    path("profile/",  profile,                name="profile"),

    path("posts/", PostListView.as_view(), name="post-list"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),  
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),  
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),

    path("post/<int:pk>/comments/new/", CommentCreateView.as_view(), name="comment-create"),
    path("comment/<int:pk>/update/", CommentUpdateView.as_view(), name="comment-update"),
    path("comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment-delete"),

    path('', views.post_list, name='post_list'),
    path('tags/<slug:slug>/', views.posts_by_tag, name='posts_by_tag'),
    path('search/', views.post_list, name='search'),

]
