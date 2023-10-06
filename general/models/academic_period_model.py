
from django.utils import timezone
from django.db import models
from general.utils.constants import STATUS_CHOICES


class AcademicPeriodModel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    created = models.DateTimeField(default=timezone.now, editable=False)
    modified = models.DateTimeField(default=timezone.now, editable=False)
    class Meta:
        verbose_name = ('Academic Period')
        verbose_name_plural = ('Academic Periods')
    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(AcademicPeriodModel, self).save(*args, **kwargs)
