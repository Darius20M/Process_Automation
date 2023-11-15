from django.utils import timezone
from django.db import models
from general.utils.constants import STATUS_CHOICES


class ClassModel(models.Model):
    student = models.ForeignKey('accounts.StudentProfileModel', on_delete=models.PROTECT)
    subject = models.ForeignKey('general.SubjectModel', on_delete=models.PROTECT)
    teacher = models.ForeignKey('accounts.TeacherModel', on_delete=models.PROTECT, null=True)
    period = models.ForeignKey('general.AcademicPeriodModel', on_delete=models.PROTECT)
    is_tutoring_now = models.BooleanField(blank=True, default=False, null=False)
    secc = models.CharField(max_length=10, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='due')
    created = models.DateTimeField(default=timezone.now, editable=False)
    modified = models.DateTimeField(default=timezone.now, editable=False)
    def __str__(self):
        return self.subject.name
    class Meta:
        verbose_name = ('Class')
        verbose_name_plural = ('Classes')
    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(ClassModel, self).save(*args, **kwargs)
