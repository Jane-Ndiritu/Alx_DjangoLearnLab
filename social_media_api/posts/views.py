from rest_framework.generics import get_object_or_404
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Post, Like
from notifications.models import Notification
from ..accounts.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def _get_post(self, pk):
        """Helper method to fetch post or raise 404"""
        return get_object_or_404(Post, pk=pk)

    def _create_notification(self, actor, verb, target, recipient):
        """Helper method to create a notification"""
        if actor != recipient:
            Notification.objects.create(actor=actor, verb=verb, target=target, recipient=recipient)

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        post = self._get_post(pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if created:
            self._create_notification(actor=request.user, verb='liked your post', target=post, recipient=post.author)
            return Response({'status': 'post liked'}, status=status.HTTP_201_CREATED)
        return Response({'status': 'already liked'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def unlike(self, request, pk=None):
        post = self._get_post(pk)
        like_qs = Like.objects.filter(user=request.user, post=post)
        if like_qs.exists():
            like_qs.delete()
            return Response({'status': 'post unliked'}, status=status.HTTP_200_OK)
        return Response({'status': 'not liked yet'}, status=status.HTTP_400_BAD_REQUEST)
