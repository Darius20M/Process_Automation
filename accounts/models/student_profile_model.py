from django.db import models
from django.utils import timezone
from django.conf import settings


class StudentProfileModel(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='student', on_delete=models.PROTECT)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=9, unique=True)
    date_of_birth = models.DateField()
    career = models.ForeignKey('general.CareerModel',on_delete=models.PROTECT)
    role = models.ForeignKey('accounts.RoleModel',on_delete=models.PROTECT)
    gender = models.CharField(max_length=10, choices=(('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')))
    address = models.TextField()
    contact_phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    identification_number = models.CharField(max_length=20, unique=True)
    enrollment_date = models.DateTimeField(default=timezone.now, editable=False)
    enrollment_status = models.CharField(max_length=20, default='N/A', choices=(('Enrolled', 'Enrolled'), ('Graduated', 'Graduated')))
    created = models.DateTimeField(default=timezone.now, editable=False)
    modified = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        verbose_name = ('Student')
        verbose_name_plural = ('Students')

    def __str__(self):
        return "{} {}".format(self.first_name, self.student_id)
    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(StudentProfileModel, self).save(*args, **kwargs)
