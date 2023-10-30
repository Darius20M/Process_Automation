from django.contrib import admin

from catalog.models import ClassModel, SubjectStudentModel
from orders.handlers import send_email_handler
from orders.models import RequesttutoringModel
from django.utils import timezone

from sequences import get_next_value

from security.handlers import create_activity_handler, create_notification_handler


class RequesttutoringModelAdmin(admin.ModelAdmin):
    list_display = ('request_number', 'subject', 'period', 'user', 'career', 'status', 'user_verified', 'comment')
    list_filter = ('status', 'subject', 'career')
    search_fields = ('request_number', 'user__username', 'user__first_name', 'user__last_name', 'user__email')
    list_per_page = 20
    list_editable = ('comment', 'status')

    fieldsets = (
        ('Request Information', {
            'fields': ('subject', 'user', 'career', 'request_number', 'status', 'user_verified', 'comment'),
        }),

    )

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

                default_comment = 'Your application was accepted for the subject {}'.format(item.subject.name)

                item.comment = default_comment
                item.save()
                create_activity_handler(
                    user=item.user,
                    level='INFO',
                    activity_text='TUTORING_REQUEST_ACCEPTED'
                )

                create_notification_handler(
                    user=item.user,
                    title='tutoring request accepted',
                    message=default_comment,
                    level='INFO'
                )
                send_email_handler(item, 'approval')


    def mark_as_Deny(self, request, queryset):

        for item in queryset:
            if item.status != 'denied':  # Verifica si no está marcado como "aceptado"
                item.status = 'denied'
                item.user_verified = request.user

                default_comment = 'Your application was denied for the subject {}'.format(item.subject.name)
                item.comment = default_comment
                item.save()
                create_activity_handler(
                    user=item.user,
                    level='INFO',
                    activity_text='TUTORING_REQUEST_DENIED'
                )

                create_notification_handler(
                    user=item.user,
                    title='tutoring request denied',
                    message=default_comment,
                    level='INFO'
                )
                send_email_handler(item, 'deny')


    mark_as_Approve.short_description = "Approve request"
    mark_as_Deny.short_description = "Deny request"

    actions = [mark_as_Approve, mark_as_Deny]

    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.request_number = "RT{0}".format(get_next_value("request_tutoring", initial_value=1000))
        obj.modified = timezone.now()
        super().save_model(request, obj, form, change)

    def get_readonly_fields(self, request, obj=None):
        # Retorna una lista de campos de solo lectura cuando se está editando un registro existente
        if obj:
            return ['request_number', 'subject', 'user', 'career', 'created', 'modified']

        return []

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj is None:
            # Cuando se está creando un nuevo registro, se permiten todas las opciones de usuarios.
            return form
        # Cuando se está editando un registro existente, limitamos las opciones de user_verified al usuario actual.
        form.base_fields['user_verified'].queryset = form.base_fields['user_verified'].queryset.filter(
            pk=request.user.pk)
        return form


admin.site.register(RequesttutoringModel, RequesttutoringModelAdmin)
