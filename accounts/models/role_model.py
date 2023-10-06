from django.db import models
from django.utils import timezone

class RoleModel(models.Model):
    name = models.CharField(max_length=180, null=False, blank=False)
    code = models.CharField(max_length=30, null=False, blank=False, unique=True)
    is_enabled = models.BooleanField(default=True)
    about = models.TextField(null=True, blank=True)
    created = models.DateTimeField(default=timezone.now, editable=False)
    modified = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        verbose_name = ('Role')
        verbose_name_plural = ('Roles')
    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(RoleModel, self).save(*args, **kwargs)
