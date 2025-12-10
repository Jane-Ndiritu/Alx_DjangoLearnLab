from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticated
from django.contrib.auth.models import User
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class IsOwnerOrReadOnly(BasePermission):
    """
    Object-level permission to only allow owners of an object to edit or delete it.
    Read-only requests are allowed for any request.
    """
    
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        if request.method in SAFE_METHODS:
            return True
        # Write permissions are only allowed to the owner
        return obj.author == request.user

class PostViewSet(viewsets.ModelViewSet):
    """
    ViewSet for CRUD operations on Posts.
    Only the author can update or delete their posts.
    """
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)  # Set the author automatically

class CommentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for CRUD operations on Comments.
    Only the author can update or delete their comments.
    """
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)  # Set the author automatically