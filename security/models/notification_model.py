from django.conf import settings
from django.db import models
from django.utils import timezone


class NotificationModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='notifications', on_delete=models.CASCADE)
    level = models.CharField(max_length=30, default="Information")
    title = models.CharField(max_length=255, null=False, blank=False)
    request_n = models.CharField(max_length=100, null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    unread = models.BooleanField(default=True)
    created = models.DateTimeField(default=timezone.now, editable=False)
    modified = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        db_table = 'sec_notifications_t'
        app_label = 'security'

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(NotificationModel, self).save(*args, **kwargs)
