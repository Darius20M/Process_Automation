from django.contrib import admin
from accounts.models import DeanModel

class DeanModelAdmin(admin.ModelAdmin):
    list_display = ('dean_id', 'first_name', 'last_name', 'date_of_birth', 'role', 'gender', 'address', 'contact_phone', 'email', 'identification_number', 'enrollment_date', 'enrollment_status', 'created', 'modified')
    list_filter = ('role', 'enrollment_status', 'gender')
    search_fields = ('dean_id', 'first_name', 'last_name', 'email')
    list_per_page = 20  # Opcional: Número de registros a mostrar por página en la vista de lista

    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name','user','date_of_birth', 'gender', 'address', 'contact_phone', 'email', 'identification_number'),
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



admin.site.register(DeanModel, DeanModelAdmin)