# post/tasks.py
from celery import shared_task
from django.core.mail import send_mail
from post.models import Comment

@shared_task
def send_comment_notification(comment_id):
    comment = Comment.objects.get(pk=comment_id)
    
    subject = 'New Comment on Your Post'
    message = f'Hello {comment.post.author.username},\n\n' \
              f'There is a new comment on your post "{comment.post.title}".\n\n' \
              f'Comment: {comment.content}\n\n' \
              f'Visit the post: {comment.post.get_absolute_url()}'
    from_email = 'your_email@example.com'
    recipient_list = [comment.post.author.email]

    send_mail(subject, message, from_email, recipient_list)
