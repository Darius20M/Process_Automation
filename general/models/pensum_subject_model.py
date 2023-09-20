# prerequisite = models.CharField(max_length=10)


from django.db import models
from django.utils import timezone

from general.utils.constants import STATUS_CHOICES


class PensumSubjectModel(models.Model):
    subject = models.ForeignKey('general.SubjectModel', on_delete=models.PROTECT,related_name='pensum_subjects')
    pensum = models.ForeignKey('general.PensumModel', on_delete=models.PROTECT)
    prerequisites = models.ForeignKey('general.SubjectModel', on_delete=models.PROTECT, blank=True, null=True,related_name='prerequisite_subjects')
    period = models.IntegerField(default=0, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    created = models.DateTimeField(default=timezone.now, editable=False)
    modified = models.DateTimeField(default=timezone.now, editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(PensumSubjectModel, self).save(*args, **kwargs)
