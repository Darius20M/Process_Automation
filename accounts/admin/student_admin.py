from django.contrib import admin

from django.contrib import admin
from accounts.models import StudentProfileModel

class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'first_name', 'last_name', 'role', 'enrollment_status')
    list_filter = ('role', 'enrollment_status', 'gender')
    search_fields = ('student_id', 'first_name', 'last_name', 'email')
    list_per_page = 20  # Opcional: Número de registros a mostrar por página en la vista de lista

    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name','user','career', 'last_name', 'student_id', 'date_of_birth', 'gender', 'address', 'contact_phone', 'email', 'identification_number'),
        }),
        ('Enrollment Information', {
            'fields': ('role', 'enrollment_date', 'enrollment_status'),
        }),
    )

    readonly_fields = ('enrollment_date', 'created', 'modified')

    def get_readonly_fields(self, request, obj=None):
        # Los campos de solo lectura dependen del estado de 'enrollment_status'
        if obj and obj.enrollment_status == 'Graduated':
            return self.readonly_fields + ('enrollment_status',)
        return self.readonly_fields

admin.site.register(StudentProfileModel, StudentProfileAdmin)
