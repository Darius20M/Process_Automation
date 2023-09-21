from django.conf import settings
from django.db import models
from django.utils import timezone

from orders.utils.constants import VERIFICATION_STATUS
from sequences import get_next_value


class RequesttutoringModel(models.Model):
    subject = models.ForeignKey('general.SubjectModel', on_delete=models.PROTECT)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='verify_requests_t', on_delete=models.CASCADE)
    career = models.ForeignKey('general.CareerModel', on_delete=models.PROTECT)
    request_number = models.CharField(max_length=180, unique=True)
    reason=models.TextField(null=True, blank=True)
    status = models.CharField(max_length=30, choices=VERIFICATION_STATUS, default=VERIFICATION_STATUS.pending,
                              null=False, blank=False)
    user_verified = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='request_verified_t',
                                      on_delete=models.PROTECT, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    created = models.DateTimeField(default=timezone.now, editable=False)
    modified = models.DateTimeField(default=timezone.now, editable=False)


    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
            self.request_number = "RT{0}".format(get_next_value("request_tutoring", initial_value=1000)
            )
        self.modified = timezone.now()
        return super(RequesttutoringModel, self).save(*args, **kwargs)