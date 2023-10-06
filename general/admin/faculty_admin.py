from django.contrib import admin
from general.models import FacultyModel

class FacultyModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'dean', 'established_date', 'website', 'contact_email', 'phone_number', 'location', 'created', 'modified')
    list_filter = ('dean',)
    search_fields = ('name', 'description')
    list_per_page = 20

    fieldsets = (
        ('Faculty Information', {
            'fields': ('name', 'dean', 'description', 'established_date', 'website', 'contact_email', 'phone_number', 'location'),
        }),
        ('Timestamps', {
            'fields': ('created', 'modified'),
        }),
    )

    readonly_fields = ('created', 'modified')

admin.site.register(FacultyModel, FacultyModelAdmin)
