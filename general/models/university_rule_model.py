
from django.db import models
from django.utils import timezone

class UniversityRuleModel(models.Model):
    min_of_credit_tutoring = models.PositiveIntegerField(default=0)
    max_of_sub_tutoring = models.PositiveIntegerField(default=0)
    max_student_become_special = models.PositiveIntegerField(default=0)
    min_student_secc = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(default=timezone.now, editable=False)
    modified = models.DateTimeField(default=timezone.now, editable=False)


    class Meta:
        verbose_name = ('University Rule')
        verbose_name_plural = ('University Rules')

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(UniversityRuleModel, self).save(*args, **kwargs)
