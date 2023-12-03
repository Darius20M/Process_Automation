from django.contrib import admin
from django.contrib.auth.models import User

from django.contrib import admin

from accounts.handlers import is_user_already
from accounts.models import StudentProfileModel, RoleModel
from catalog.models import SubjectStudentModel
from general.models import PensumSubjectModel
from orders.handlers import send_email_handler


class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'full_name', 'date_of_birth', 'career', 'email', 'gender', 'enrollment_status')
    list_filter = ('role', 'student_id', 'enrollment_status', 'gender')
    search_fields = ('student_id', 'first_name', 'last_name', 'email')
    list_per_page = 20

    fieldsets = (
        ('Personal Information', {
            'fields': (
             'student_id', 'first_name', 'last_name','career', 'date_of_birth', 'gender', 'address', 'contact_phone',
            'email', 'identification_number'),
        }),
        ('Enrollment Information', {
            'fields': ('role', 'enrollment_date', 'enrollment_status'),
        }),
    )

    readonly_fields = ('enrollment_date', 'student_id', 'created', 'modified')

    def full_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name)

    full_name.short_description = 'Full name'

    def save_model(self, request, obj, form, change):

        if change:
            obj.user.email = obj.email
            obj.user.first_name = obj.first_name
            obj.user.last_name = obj.last_name
            obj.user.save()
            obj.save()
        else:
            username = is_user_already()
            user = User.objects.create_user(
                username=username,
                email=obj.email,
                password=username,
                first_name=obj.first_name,
                last_name=obj.last_name
            )
            obj.user = user
            obj.student_id = username
            obj.save()
            pensum = obj.career.pensum
            pensum_sub = PensumSubjectModel.objects.filter(pensum=pensum)

            for i in pensum_sub:
                SubjectStudentModel.objects.create(
                    subject=i.subject,
                    student=obj
                )
            send_email_handler(obj, 'user_creation')


        super().save_model(request, obj, form, change)

    def get_readonly_fields(self, request, obj=None):
        # Los campos de solo lectura dependen del estado de 'enrollment_status'
        if obj and obj.enrollment_status == 'Graduated':
            return self.readonly_fields + ('enrollment_status',)
        return self.readonly_fields


admin.site.register(StudentProfileModel, StudentProfileAdmin)
