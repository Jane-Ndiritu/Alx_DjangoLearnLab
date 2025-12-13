from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedView

router = DefaultRouter()
router.register(r'', PostViewSet)
router.register('posts', PostViewSet, basename='posts')
router.register('comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('', FeedView.as_view(), name='feed'),
    path('<int:pk>/like/', LikePostView.as_view(), name='like-post'),
    path('<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike-post'),
    path('comments/', CommentViewSet.as_view({'get': 'list', 'post': 'create'}), name='comments'),
    path('', include(router.urls)),
]

urlpatterns += router.urls
