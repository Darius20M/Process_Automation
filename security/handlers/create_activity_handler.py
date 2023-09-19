from django.contrib.auth.models import User

from security.models import ActivityModel


def create_activity_handler(user: User, activity_text: str, level: str = 'INFO'):
    activity = ActivityModel.objects.create(
        user=user,
        level=level,
        activity_text=activity_text
    )
    return activity
