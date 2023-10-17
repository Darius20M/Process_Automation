from django.contrib import admin
from accounts.models import TeacherModel

class TeacherModelAdmin(admin.ModelAdmin):
    list_display = ('teacher_id', 'full_name','email','school', 'date_of_birth', 'gender','enrollment_status')
    list_filter = ('teacher_id','school','enrollment_status', 'gender')
    search_fields = ('teacher_id', 'first_name', 'last_name', 'email')
    list_per_page = 20  # Opcional: Número de registros a mostrar por página en la vista de lista

    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'teacher_id', 'date_of_birth', 'gender', 'address', 'school','contact_phone', 'email', 'identification_number'),
        }),
        ('Enrollment Information', {
            'fields': ('role', 'enrollment_date', 'enrollment_status'),
        }),
    )

    def full_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name)

    full_name.short_description = 'Full name'

    readonly_fields = ('enrollment_date', 'created', 'modified')

    def get_readonly_fields(self, request, obj=None):
        # Los campos de solo lectura dependen del estado de 'enrollment_status'
        if obj and obj.enrollment_status == 'Graduated':
            return self.readonly_fields + ('enrollment_status',)
        return self.readonly_fields

admin.site.register(TeacherModel, TeacherModelAdmin)
