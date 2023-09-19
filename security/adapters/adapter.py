from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.models import EmailConfirmation
from allauth.account.adapter import DefaultAccountAdapter

from security.handlers import create_activity_handler, create_notification_handler
from django.utils.translation import gettext as _


class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=False):
        user = super().save_user(request, user, form, commit)
        user.save()

        # Register activity
        create_activity_handler(
            user=user,
            activity_text=_('Registration on the platform'),
            level='INFO'
        )
        # create notification
        create_notification_handler(
            user=user,
            title=_('Welcome Email'),
            message=_('We have sent an email for mail verification.'),
            level='INFO'
        )

        return user
    def send_mail(self, template_prefix, email, context, subject=None):
        context['EMAIL_TO'] = email
        msg = self.render_mail(template_prefix, email, context)
        subject = "Somenthing here"

        if subject:
            msg.subject = subject

        msg.send()