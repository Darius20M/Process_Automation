from django.contrib import admin
from accounts.models import DeanModel
from django.utils.html import format_html
class DeanModelAdmin(admin.ModelAdmin):
    list_display = ('enrollment', 'full_name','faculty_name', 'date_of_birth', 'role', 'gender', 'contact_phone','email')
    list_filter = ('enrollment_status', 'gender')
    search_fields = ('dean_id', 'first_name', 'last_name', 'email')
    list_per_page = 20  # Opcional: Número de registros a mostrar por página en la vista de lista

    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name','date_of_birth', 'gender', 'address', 'contact_phone', 'email', 'identification_number'),
        }),
        ('Enrollment Information', {
            'fields': ('role', 'enrollment_date', 'enrollment_status'),
        }),
    )
    readonly_fields = ('enrollment_date', 'created', 'modified')

    def enrollment(self, obj):
        return obj.dean_id

    def full_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name)

    full_name.short_description = 'Full name'
    enrollment.short_description = 'Enrollment'

    def faculty_name(self, obj):
        return ', '.join([faculty.name for faculty in obj.faculties.all()])

    faculty_name.short_description = 'Faculty'

    def get_readonly_fields(self, request, obj=None):
        # Los campos de solo lectura dependen del estado de 'enrollment_status'
        if obj and obj.enrollment_status == 'Graduated':
            return self.readonly_fields + ('enrollment_status',)
        return self.readonly_fields



admin.site.register(DeanModel, DeanModelAdmin)