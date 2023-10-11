from django.contrib import admin
from general.models import SchoolModel

class SchoolModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'director', 'faculty', 'established_date', 'website', 'contact_email', 'phone_number')
    list_filter = ('faculty',)
    search_fields = ('name', 'description')
    list_per_page = 20

    fieldsets = (
        ('School Information', {
            'fields': ('name', 'director', 'faculty', 'description', 'established_date', 'website', 'contact_email', 'phone_number', 'location'),
        }),
        ('Timestamps', {
            'fields': ('created', 'modified'),
        }),
    )

    readonly_fields = ('created', 'modified')

admin.site.register(SchoolModel, SchoolModelAdmin)
