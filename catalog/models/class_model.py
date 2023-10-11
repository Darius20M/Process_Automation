

from django.utils import timezone
from django.db import models
from general.utils.constants import STATUS_CHOICES


class ClassModel(models.Model):
    subject = models.ForeignKey('general.SubjectModel', on_delete=models.PROTECT)
    teacher = models.ForeignKey('accounts.TeacherModel', on_delete=models.PROTECT)
    period = models.ForeignKey('general.AcademicPeriodModel', on_delete=models.PROTECT)
    secc = models.CharField(max_length=10, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    created = models.DateTimeField(default=timezone.now, editable=False)
    modified = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        verbose_name = ('Class')
        verbose_name_plural = ('Classes')
    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(ClassModel, self).save(*args, **kwargs)
