from django.db import models
from django.conf import settings
from django.utils import timezone

User = settings.AUTH_USER_MODEL

class Notification(models.Model):
    actor = models.ForeignKey(
        User,
        related_name='notifications_sent',
        on_delete=models.CASCADE
    )  # Who triggered the notification

    verb = models.CharField(max_length=255)  # What happened, e.g., "liked your post"
    target = models.ForeignKey(
        'posts.Post',  # Or another model that is the target
        related_name='notifications',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    recipient = models.ForeignKey(
        User,
        related_name='notifications',
        on_delete=models.CASCADE
    )  # Who receives the notification

    timestamp = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)  # Optional: track read/unread

    def __str__(self):
        return f'{self.actor} {self.verb} {self.target} for {self.recipient}'
