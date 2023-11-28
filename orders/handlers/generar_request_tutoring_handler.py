from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import APIException
from rest_framework import status

from accounts.models import StudentProfileModel
from catalog.models import SubjectStudentModel
from general.models import SubjectModel, AcademicPeriodModel, UniversityRuleModel
from orders.handlers.is_subject_available_handler import is_subject_available_handler
from orders.models import RequesttutoringModel
from orders.utils.constants import VERIFICATION_STATUS
from security.handlers import create_activity_handler, create_notification_handler


def generate_request_tutoring_handler(
        subject: SubjectModel,
        shift,
        period: AcademicPeriodModel,
        student: StudentProfileModel,
        user
) -> RequesttutoringModel:

    if StudentProfileModel.objects.get(user=user).enrollment_status != 'Enrolled':
        raise APIException(detail="No estas activo para realizar tutorias", code=status.HTTP_400_BAD_REQUEST)

    if is_subject_available_handler(subject, user):
        raise APIException(detail="Aun no has completado el prerequisito de esta materia", code=status.HTTP_400_BAD_REQUEST)
    # para el minimode materia que tiene que tener
    if SubjectStudentModel.objects.filter(student__user=user,status='due').count() > UniversityRuleModel.objects.get(
            id=1).q_of_subj_tutoring:
        raise APIException(detail="Aun no has completado el minimo de materias para tomar tutorias", code=status.HTTP_400_BAD_REQUEST)

    # para el max de materia que tiene aprovada en tutoria
    if RequesttutoringModel.objects.filter(user=user, period=period,
                                           status=VERIFICATION_STATUS.accepted).count() >= UniversityRuleModel.objects.get(
        id=1).max_by_sub_tutoring:
        raise APIException(detail="Tienes el maximo de tutoria aceptada para este periodo", code=status.HTTP_400_BAD_REQUEST)

    # para el max de materia que tiene pend8iente en tutoria
    if RequesttutoringModel.objects.filter(user=user, period=period,
                                           status=VERIFICATION_STATUS.pending).count() >= UniversityRuleModel.objects.get(
        id=1).max_by_sub_tutoring:
        raise APIException(detail="Has alcanzado el maximo de solicitudes pendientes para este periodo", code=status.HTTP_400_BAD_REQUEST)

    # para saber si tiene aprovada tutoria
    if RequesttutoringModel.objects.filter(user=user, period=period, subject=subject,
                                           status=VERIFICATION_STATUS.accepted).exists():
        raise APIException(detail="This subject was accepted", code=status.HTTP_400_BAD_REQUEST)

    # para saber si tiene pendiente tutoria
    if RequesttutoringModel.objects.filter(user=user, period=period, subject=subject,
                                           status=VERIFICATION_STATUS.pending).exists():
        raise APIException(detail="Ya tienes una solicitud de esta materia pendiente de aceptacion", code=status.HTTP_400_BAD_REQUEST)

    request_tutoring = RequesttutoringModel.objects.create(
        subject=subject,
        user=user,
        career=student.career,
        period=period
    )

    request = RequesttutoringModel.objects.filter(period=period, subject=subject, status='pending')
    if request.count() >= UniversityRuleModel.objects.get(
            id=1).min_student_become_special:
        request.update(is_special_course = True)


    create_activity_handler(
        user=user,
        level='INFO',
        activity_text='TUTORING_REQUEST'
    )

    message_text = 'Has enviando una solicitud de tutoria para la materia: {}'.format(subject.name)

    create_notification_handler(
        user=user,
        title=_('tutoring request sent'),
        message=message_text,
        level='INFO'
    )

    return request_tutoring
