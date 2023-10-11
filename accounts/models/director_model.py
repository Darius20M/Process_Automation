from django.db import models
from django.utils import timezone
from django.conf import settings


class DirectorModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    director_id = models.CharField(max_length=10, unique=True)
    date_of_birth = models.DateField()
    role = models.ForeignKey('accounts.RoleModel', on_delete=models.PROTECT)
    gender = models.CharField(max_length=10, choices=(('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')))
    address = models.TextField()
    contact_phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    identification_number = models.CharField(max_length=20, unique=True)
    enrollment_date = models.DateTimeField(default=timezone.now, editable=False)
    enrollment_status = models.CharField(max_length=20, choices=(('Enrolled', 'Enrolled'), ('Inactive', 'Inactive')))
    created = models.DateTimeField(default=timezone.now, editable=False)
    modified = models.DateTimeField(default=timezone.now, editable=False)
    class Meta:
        verbose_name = ('Director')
        verbose_name_plural = ('Directors')
    def __str__(self):
        return "{} {}".format(self.first_name, self.director_id)
    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(DirectorModel, self).save(*args, **kwargs)
