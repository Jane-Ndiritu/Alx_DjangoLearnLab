from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView,
    add_comment_view, update_comment_view, delete_comment_view
)
from . import views

urlpatterns = [
    # POSTS
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

    path('post/<int:pk>/comments/new/', add_comment_view, name='comment_create'),
    path('comment/<int:pk>/update/', update_comment_view, name='comment_update'),
    path('comment/<int:pk>/delete/', delete_comment_view, name='comment_delete'),
]
