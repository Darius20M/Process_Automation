from django.db import models
from django.utils import timezone


class DirectorModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    director_id = models.CharField(max_length=8, unique=True)
    date_of_birth = models.DateField()
    role = models.ForeignKey('accounts.RoleModel', on_delete=models.PROTECT)
    gender = models.CharField(max_length=10, choices=(('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')))
    address = models.TextField()
    contact_phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    identification_number = models.CharField(max_length=20, unique=True)
    enrollment_date = models.DateTimeField(default=timezone.now, editable=False)
    enrollment_status = models.CharField(max_length=20, choices=(('Enrolled', 'Enrolled'), ('Graduated', 'Graduated')))
    created = models.DateTimeField(default=timezone.now, editable=False)
    modified = models.DateTimeField(default=timezone.now, editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(DirectorModel, self).save(*args, **kwargs)