from django.contrib import admin
from accounts.models import DirectorModel


class DirectorModelAdmin(admin.ModelAdmin):
    list_display = (
        'enrollment', 'full_name', 'school_name', 'date_of_birth', 'role', 'gender', 'contact_phone', 'email',
        'identification_number')
    list_filter = ('role', 'enrollment_status', 'gender')
    search_fields = ('director_id', 'first_name', 'last_name', 'email')
    list_per_page = 20  # Opcional: Número de registros a mostrar por página en la vista de lista

    fieldsets = (
        ('Personal Information', {
            'fields': (
                'first_name', 'last_name',  'director_id', 'date_of_birth', 'gender', 'address', 'contact_phone',
                'email', 'identification_number'),
        }),
        ('Enrollment Information', {
            'fields': ('role', 'enrollment_date', 'enrollment_status'),
        }),
    )

    readonly_fields = ('enrollment_date', 'created', 'modified')


    def enrollment(self, obj):
        return obj.director_id

    def school_name(self, obj):
        return ', '.join([schools.name for schools in obj.schools.all()])

    def full_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name)

    school_name.short_description = 'School'
    full_name.short_description = 'Full name'
    enrollment.short_description = 'Enrollment'



    def get_readonly_fields(self, request, obj=None):
        if obj and obj.enrollment_status == 'Enrolled':
            return self.readonly_fields + ('enrollment_status',)
        return self.readonly_fields


admin.site.register(DirectorModel, DirectorModelAdmin)
