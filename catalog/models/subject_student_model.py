

from django.utils import timezone
from django.db import models
from general.utils.constants import STATUS_CHOICES
#hacer modelo historico general

class SubjectStudentModel(models.Model):
    subject = models.ForeignKey('general.SubjectModel', related_name='subject_student', on_delete=models.CASCADE)
    student = models.ForeignKey('accounts.StudentProfileModel', related_name='subject_student', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='due')
    created = models.DateTimeField(default=timezone.now, editable=False)
    modified = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        verbose_name = ('Subject Student')
        verbose_name_plural = ('Subject Students')
    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(SubjectStudentModel, self).save(*args, **kwargs)
