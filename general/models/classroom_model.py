from django.db import models
from django.utils import timezone

from general.utils.constants import STATUS_CHOICES


class ClassroomModel(models.Model):
    code = models.CharField(max_length=10, unique=True)
    capacity = models.PositiveIntegerField()
    building = models.CharField(max_length=100)
    floor = models.PositiveIntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    created = models.DateTimeField(default=timezone.now, editable=False)
    modified = models.DateTimeField(default=timezone.now, editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(ClassroomModel, self).save(*args, **kwargs)
