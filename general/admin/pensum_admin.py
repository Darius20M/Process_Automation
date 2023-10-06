from django.contrib import admin
from general.models import PensumModel

class PensumModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'school', 'start_year', 'end_year', 'total_credits', 'total_hours', 'total_hours_p', 'total_hours_t', 'total_subject', 'version', 'status', 'created', 'modified')
    list_filter = ('status', 'school')
    search_fields = ('name', 'description')
    list_per_page = 20

    fieldsets = (
        ('Pensum Information', {
            'fields': ('name', 'school', 'start_year', 'end_year', 'total_credits', 'total_hours', 'total_hours_p', 'total_hours_t', 'total_subject', 'description', 'version', 'status'),
        }),
        ('Timestamps', {
            'fields': ('created', 'modified'),
        }),
    )

    readonly_fields = ('created', 'modified')

admin.site.register(PensumModel, PensumModelAdmin)
