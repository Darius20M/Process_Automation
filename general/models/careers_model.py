from django.db import models
from django.utils import timezone

from general.utils.constants import STATUS_CHOICES


class CareerModel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    pensum = models.ForeignKey('general.PensumModel', on_delete=models.PROTECT)
    degree = models.CharField(max_length=100)
    duration_in_semesters = models.PositiveIntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    created = models.DateTimeField(default=timezone.now, editable=False)
    modified = models.DateTimeField(default=timezone.now, editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(CareerModel, self).save(*args, **kwargs)

