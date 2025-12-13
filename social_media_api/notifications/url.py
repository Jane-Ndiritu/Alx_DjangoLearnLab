from django.urls import path,include
from .views import UserNotificationsView, MarkNotificationsReadView

urlpatterns = [
    path('', UserNotificationsView.as_view(), name='user-notifications'),
     path('', NotificationListView.as_view(), name='notifications-list'),
    path('mark-read/', MarkNotificationsReadView.as_view(), name='mark-notifications-read'),
]
