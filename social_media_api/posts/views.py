from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.db.models import Q
from .models import Post
from ..accounts.serializers import PostSerializer

class FeedView(generics.ListAPIView):
    """
    View to show posts from users that the current user follows
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated] 
    
    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')