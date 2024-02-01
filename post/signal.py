# post/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from practic.tasks import send_comment_notification
from .models import Comment

@receiver(post_save, sender=Comment)
def send_comment_notification_on_save(sender, instance, **kwargs):
    send_comment_notification.delay(instance.id)
