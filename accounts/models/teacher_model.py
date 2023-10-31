from django.db import models
from django.utils import timezone
from django.conf import settings



class TeacherModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    teacher_id = models.CharField(max_length=10, unique=True)
    date_of_birth = models.DateField()
    school = models.ForeignKey('general.SchoolModel',on_delete=models.PROTECT)
    role = models.ForeignKey('accounts.RoleModel',on_delete=models.PROTECT)
    gender = models.CharField(max_length=10, choices=(('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')))
    address = models.TextField()
    contact_phone = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    identification_number = models.CharField(max_length=30, unique=True)
    enrollment_date = models.DateTimeField(default=timezone.now, editable=False)
    enrollment_status = models.CharField(max_length=20, choices=(('Enrolled', 'Enrolled'), ('Graduated', 'Graduated')))
    created = models.DateTimeField(default=timezone.now, editable=False)
    modified = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        verbose_name = ('Teacher')
        verbose_name_plural = ('Teachers')
    def __str__(self):
        return "{} {}".format(self.first_name, self.teacher_id)
    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(TeacherModel, self).save(*args, **kwargs)
