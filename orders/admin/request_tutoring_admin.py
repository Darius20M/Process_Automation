from django.contrib import admin, messages
from rest_framework.exceptions import APIException
from django.db.models import F

from accounts.models import StudentProfileModel
from catalog.models import ClassModel, SubjectStudentModel
from general.models import UniversityRuleModel, SubjectModel
from orders.handlers import send_email_handler, is_subject_available_handler
from orders.models import RequesttutoringModel
from django.utils import timezone
from rest_framework import status

from sequences import get_next_value

from orders.utils.constants import VERIFICATION_STATUS
from security.handlers import create_activity_handler, create_notification_handler
from security.models import NotificationModel


class RequesttutoringModelAdmin(admin.ModelAdmin):
    list_display = ('request_number', 'subject', 'period', 'user', 'career', 'status', 'user_verified','is_special_course','comment')
    list_filter = ('status', 'subject', 'user','period','career')
    search_fields = ('request_number', 'user__username', 'user__first_name', 'user__last_name', 'user__email')
    list_per_page = 20
    list_editable = ('comment', 'status')
    fieldsets = (
        ('Request Information', {
            'fields': ('subject', 'user', 'career', 'period','status', 'user_verified', 'comment'),
        }),

    )
    readonly_fields = ('request_number',)

    def mark_as_Approve(self, request, queryset):

        for item in queryset:
            if item.status != 'accepted':  # Verifica si no está marcado como "aceptado"
                item.status = 'accepted'
                item.user_verified = request.user
                student = item.user.student

                ClassModel.objects.create(
                    student=student,
                    subject=item.subject,
                    period=item.period
                )

                subject_student = SubjectStudentModel.objects.get(student=student,subject=item.subject)
                subject_student.status = 'ongoing'
                subject_student.save()

                default_comment = 'Tu solicitud fue aceptada para la materia: {}'.format(item.subject.name)

                item.comment = default_comment
                item.save()
                create_activity_handler(
                    user=item.user,
                    level='INFO',
                    activity_text='TUTORING_REQUEST_ACCEPTED'
                )

                create_notification_handler(
                    user=item.user,
                    title='Solicitud de tutorias aprobada',
                    request_n=item.request_number,
                    message=default_comment,
                    level='INFO'
                )
                request = RequesttutoringModel.objects.filter(period=item.period, subject=item.subject, status='pending')
                if request.count() >= UniversityRuleModel.objects.get(
                        id=1).min_student_become_special:
                    request.update(is_special_course=True)
                send_email_handler(item, 'approval')


    def mark_as_Deny(self, request, queryset):

        for item in queryset:
            if item.status != 'denied':  # Verifica si no está marcado como "aceptado"
                item.status = 'denied'
                item.user_verified = request.user

                default_comment = 'Tu solicitud fue negada para la asignatura {}'.format(item.subject.name)
                item.comment = default_comment
                item.save()
                create_activity_handler(
                    user=item.user,
                    level='INFO',
                    activity_text='TUTORING_REQUEST_DENIED'
                )

                create_notification_handler(
                    user=item.user,
                    title='Solicitud de tutoria denegada',
                    message=default_comment,
                    request_n=item.request_number,
                    level='INFO'
                )
                send_email_handler(item, 'deny')


    mark_as_Approve.short_description = "Approve request"
    mark_as_Deny.short_description = "Deny request"

    actions = [mark_as_Approve, mark_as_Deny]

    def save_model(self, request, obj, form, change):
        if change:

            if obj.status == 'pending':
                obj.save()
            elif obj.status == 'accepted':  # Verifica si no está marcado como "aceptado"
                obj.status = 'accepted'

                obj.user_verified = request.user
                student = obj.user.student

                ClassModel.objects.create(
                    is_tutoring_now = True,
                    student=student,
                    subject=obj.subject,
                    period=obj.period
                )

                subject_student = SubjectStudentModel.objects.get(student=student, subject=obj.subject)
                subject_student.status = 'ongoing'
                subject_student.save()

                default_comment = 'Tu solicitud fue aceptada para la materia: {}'.format(obj.subject.name)

                obj.save()
                create_activity_handler(
                    user=obj.user,
                    level='INFO',
                    activity_text='TUTORING_REQUEST_ACCEPTED'
                )
                if not NotificationModel.objects.filter(title='Solicitud de tutoria aprobada',request_n=obj.request_number).exists():
                    create_notification_handler(
                        user=obj.user,
                        title='Solicitud de tutoria aprobada',
                        message=default_comment,
                        request_n=obj.request_number,
                        level='INFO'
                    )
                request = RequesttutoringModel.objects.filter(period=obj.period, subject=obj.subject,
                                                              status='pending')
                if request.count() >= UniversityRuleModel.objects.get(
                        id=1).min_student_become_special:
                    request.update(is_special_course=True)
                send_email_handler(obj, 'approval')
            elif obj.status == 'denied':  # Verifica si no está marcado como "aceptado"
                obj.status = 'denied'
                obj.user_verified = request.user

                default_comment = 'Tu aplicacion fue negada para la asignatura {}'.format(obj.subject.name)
                obj.save()
                create_activity_handler(
                    user=obj.user,
                    level='INFO',
                    activity_text='TUTORING_REQUEST_DENIED'
                )

                create_notification_handler(
                    user=obj.user,
                    title='Solicitud de tutoria denegada',
                    message=default_comment,
                    request_n=obj.request_number,
                    level='INFO'
                )
                send_email_handler(obj, 'deny')


        else:
            has_error = False

            if StudentProfileModel.objects.get(user=obj.user).enrollment_status != 'Enrolled':
                messages.error(request, 'No puedes realizar este proceso debido a que el estudiante no esta activo')

            if not obj.subject.is_tutoring:
                messages.error(request, 'Esta materia no esta disponible para tutorias.')
                has_error = True

            if  SubjectStudentModel.objects.filter(student__user=obj.user,subject=obj.subject,status='ongoing'):
                messages.error(request, 'Esta materia ya esta siendo cursada por el estudiante.')
                has_error = True

            if not SubjectStudentModel.objects.filter(student__user=obj.user,subject=obj.subject,status='due'):
                messages.error(request, 'Esta materia ya ha sido aprobada por el estudiante.')
                has_error = True

            if is_subject_available_handler(obj.subject, obj.user):
                messages.error(request, 'Aun no ha tomado el prerequisito este estudiante.')
                has_error = True

            # para el minimode materia que tiene que tener
            if SubjectStudentModel.objects.filter(student__user=obj.user,
                                                  status='due').count() > UniversityRuleModel.objects.get(
                    id=1).q_of_subj_tutoring:
                messages.error(request, 'Aun no ha tomado el minimo de materias este estudiante.')
                has_error = True


            # para el max de materia que tiene aprobada en tutoria
            if RequesttutoringModel.objects.filter(user=obj.user, period=obj.period,
                                                   status=VERIFICATION_STATUS.accepted).count() >= UniversityRuleModel.objects.get(
                id=1).max_by_sub_tutoring:

                messages.error(request, 'Ya ha tomado el maximo de materias por periodo este estudiante.')
                has_error = True


            # para el max de materia que tiene pend8iente en tutoria
            if RequesttutoringModel.objects.filter(user=obj.user, period=obj.period,
                                                   status=VERIFICATION_STATUS.pending).count() >= UniversityRuleModel.objects.get(
                id=1).max_by_sub_tutoring:
                messages.error(request, 'Ya ha tomado el maximo de materias pendiente por periodo este estudiante.')
                has_error = True


            # para saber si tiene aprobada tutoria
            if RequesttutoringModel.objects.filter(user=obj.user, period=obj.period, subject=obj.subject,
                                                   status=VERIFICATION_STATUS.accepted).exists():
                messages.error(request, 'Ya esta materia fue aprobada para este estudiante.')
                has_error = True


            # para saber si tiene pendiente tutoria
            if RequesttutoringModel.objects.filter(user=obj.user, period=obj.period, subject=obj.subject, status=VERIFICATION_STATUS.pending).exists():
                messages.error(request, 'Ya esta materia fue solicitada y esta en proceso de aprobacion para este estudiante.')
                has_error = True

            if has_error:
                messages.set_level(request, messages.ERROR)
            else:
                super().save_model(request, obj, form, change)
                default_comment = 'Tu solicitud fue generada para la materia: {}'.format(obj.subject.name)

                create_notification_handler(
                    user=obj.user,
                    title='Solicitud de tutoria enviada',
                    message=default_comment,
                    request_n=obj.request_number,
                    level='INFO'
                )
                send_email_handler(obj, 'confirmation')

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['request_number', 'subject','career', 'created', 'modified']

        return []

    def get_form(self, request, obj=None, **kwargs):

        form = super().get_form(request, obj, **kwargs)

        form.base_fields['user_verified'].queryset = form.base_fields['user_verified'].queryset.filter(
            pk=request.user.pk)
        form.base_fields['user'].queryset = form.base_fields['user'].queryset.filter(is_staff=False,is_superuser=False)
        return form




admin.site.register(RequesttutoringModel, RequesttutoringModelAdmin)
