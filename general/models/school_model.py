from django.db import models
from django.utils import timezone

class SchoolModel(models.Model):
    name = models.CharField(max_length=100)
    director = models.ForeignKey('accounts.DirectorModel', on_delete=models.PROTECT)
    faculty = models.ForeignKey('general.FacultyModel', on_delete=models.PROTECT)
    description = models.TextField(blank=True, null=True)
    established_date = models.DateField()
    website = models.URLField(blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(default=timezone.now, editable=False)
    modified = models.DateTimeField(default=timezone.now, editable=False)
    class Meta:
        verbose_name = ('School')
        verbose_name_plural = ('Schools')
    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(SchoolModel, self).save(*args, **kwargs)
