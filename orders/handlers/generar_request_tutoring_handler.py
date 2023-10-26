from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from general.models import SubjectModel
from orders.models import RequesttutoringModel


def generate_request_tutoring_handler(
        subject:SubjectModel) -> RequesttutoringModel:

    """if RequestInvitationModel.objects.filter(practice=practice, email=email, status=INVITATION_STATUS.pending).exists():
        raise RequestInvitationPendingException()
    if RequestInvitationModel.objects.filter(practice=practice, email=email, status=INVITATION_STATUS.accepted).exsits():
        raise RequestInvitationAcceptedException()"""



    """request_tutoring = RequesttutoringModel.objects.create(
        practice=practice,
        email=email,
        role=role,
        first_name=first_name,
        last_name=last_name,
        npi=npi,
        ipa_member_id=ipa_member_id,
        requesting_user=requesting_user,
        user=user,
        status=INVITATION_STATUS.pending
    )
    # create active requesting user
    create_activity_handler(
        application=application,
        user=requesting_user,
        level='INFO',
        activity_text='REQUEST_INVITATION_MEMBER'
    )

    message_text = 'You have sent an invitation request to the {} email to join the {} practice'.format(email, practice.name)

    create_notification_handler(
        user=requesting_user,
        title=_('Invitation request sent'),
        message=message_text,
        level='INFO'
    )

    if user is not None:
        message_user = 'You have received an invitation request to join the {} practice.'.format(practice.name)
        create_notification_handler(
            user=requesting_user,
            title=_('Invitation request'),
            message=message_user,
            level='INFO'
        )
"""
    return 0