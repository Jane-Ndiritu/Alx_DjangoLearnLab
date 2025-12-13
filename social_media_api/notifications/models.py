from django.db import models
from django.conf import settings
from django.utils import timezone

User = settings.AUTH_USER_MODEL

class Notification(models.Model):
    actor = models.ForeignKey(
        User,
        related_name='notifications_sent',
        on_delete=models.CASCADE
    )  

    verb = models.CharField(max_length=255) 
    target = models.ForeignKey(
        'posts.Post',  
        related_name='notifications',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    recipient = models.ForeignKey(
        User,
        related_name='notifications',
        on_delete=models.CASCADE
    )  

    timestamp = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False) 

    def __str__(self):
        return f'{self.actor} {self.verb} {self.target} for {self.recipient}'
