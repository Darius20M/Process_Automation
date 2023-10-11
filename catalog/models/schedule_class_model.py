

from django.utils import timezone
from django.db import models
from general.utils.constants import STATUS_CHOICES


class ScheduleClassModel(models.Model):
    _class = models.ForeignKey('catalog.ClassModel', on_delete=models.PROTECT)
    classroom = models.ForeignKey('general.ClassroomModel', on_delete=models.PROTECT)
    day = models.CharField(max_length=200, null=False, blank=False)
    h_start = models.DateTimeField(null=False, blank=False)
    h_end = models.DateTimeField(null=False, blank=False)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    created = models.DateTimeField(default=timezone.now, editable=False)
    modified = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        verbose_name = ('Schedule Class')
        verbose_name_plural = ('Schedule Classes')
    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(ScheduleClassModel, self).save(*args, **kwargs)


