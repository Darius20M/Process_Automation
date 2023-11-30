from django.contrib.auth.models import User

from security.models import NotificationModel


def create_notification_handler(user: User, title: str,request_n:str, message: str, level: str = 'INFO'):
    notification = NotificationModel.objects.create(
        user=user,
        title=title,
        request_n=request_n,
        message=message,
        level=level
    )
    return notification
