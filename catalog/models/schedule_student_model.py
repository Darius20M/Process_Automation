
from django.utils import timezone
from django.db import models
from general.utils.constants import STATUS_CHOICES


class ScheduleStudentModel(models.Model):
    student = models.ForeignKey('accounts.StudentProfileModel', on_delete=models.PROTECT)
    schedule = models.ForeignKey('catalog.ScheduleClassModel', on_delete=models.PROTECT, null= True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    created = models.DateTimeField(default=timezone.now, editable=False)
    modified = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        verbose_name = ('Schedule Student')
        verbose_name_plural = ('Schedule Students')
    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(ScheduleStudentModel, self).save(*args, **kwargs)
