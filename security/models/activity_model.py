from django.conf import settings
from django.db import models
from django.utils import timezone



class ActivityModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='activities', on_delete=models.PROTECT)
    activity_text = models.TextField(null=False, blank=False)
    level = models.CharField(max_length=30, default="Information")
    created = models.DateTimeField(default=timezone.now, editable=False)
    modified = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        db_table = 'sec_activities_t'
        app_label = 'security'

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(ActivityModel, self).save(*args, **kwargs)
