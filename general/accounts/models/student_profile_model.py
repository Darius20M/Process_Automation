from django.db import models
from django.utils import timezone


class StudentProfileModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    Student_ID = models.CharField(max_length=8, unique=True)
    date_of_birth = models.DateField()
    role = models.ForeignKey('accounts.RoleModel', related_name='accounts', on_delete=models.PROTECT)
    gender = models.CharField(max_length=10, choices=(('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')))
    address = models.TextField()
    contact_phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    identification_number = models.CharField(max_length=20, unique=True)
    enrollment_date = models.DateField()
    enrollment_status = models.CharField(max_length=20, choices=(('Enrolled', 'Enrolled'), ('Graduated', 'Graduated')))

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(StudentProfileModel, self).save(*args, **kwargs)
