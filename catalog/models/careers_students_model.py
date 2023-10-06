from django.utils import timezone
from django.db import models
from general.utils.constants import STATUS_CHOICES


class CareerStudentModel(models.Model):
    student = models.ForeignKey('accounts.StudentProfileModel', on_delete=models.PROTECT)#esto deberia ser uno a uno y poner un campo user lo que dira que un user puede tener varias materi apero con otro user
    career = models.ForeignKey('general.CareerModel', on_delete=models.PROTECT)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    created = models.DateTimeField(default=timezone.now, editable=False)
    modified = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        verbose_name = ('Career Student')
        verbose_name_plural = ('Career Students')
    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(CareerStudentModel, self).save(*args, **kwargs)
