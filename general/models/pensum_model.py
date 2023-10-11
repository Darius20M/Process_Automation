
from django.db import models
from django.utils import timezone

from general.utils.constants import STATUS_CHOICES


class PensumModel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    school = models.ForeignKey('general.SchoolModel', on_delete=models.PROTECT)
    start_year = models.DateField(default=timezone.now)
    end_year = models.DateField(default=timezone.now)
    total_credits = models.PositiveIntegerField(blank=True, null=True)
    total_hours = models.PositiveIntegerField(blank=True, null=True)
    total_hours_p = models.PositiveIntegerField(blank=True, null=True)
    total_hours_t = models.PositiveIntegerField(blank=True, null=True)
    total_subject = models.PositiveIntegerField(blank=True, null=True)
    version = models.CharField(max_length=10)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    created = models.DateTimeField(default=timezone.now, editable=False)
    modified = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = ('Pensum')
        verbose_name_plural = ('Pensums')
    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(PensumModel, self).save(*args, **kwargs)