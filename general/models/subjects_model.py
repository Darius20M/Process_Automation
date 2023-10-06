from django.db import models
from django.utils import timezone


class SubjectModel(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    credits = models.PositiveIntegerField()
    to_hours = models.PositiveIntegerField()
    p_hours = models.PositiveIntegerField()
    t_hours = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=(('Active', 'Active'), ('Inactive', 'Inactive') ))
    created = models.DateTimeField(default=timezone.now, editable=False)
    modified = models.DateTimeField(default=timezone.now, editable=False)
    class Meta:
        verbose_name = ('Subject')
        verbose_name_plural = ('Subjects ')
    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(SubjectModel, self).save(*args, **kwargs)
