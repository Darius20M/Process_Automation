from django.contrib import admin
from general.models import AcademicPeriodModel

class AcademicPeriodModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'status', 'created', 'modified')
    list_filter = ('status', 'start_date')
    search_fields = ('name', 'description')
    list_per_page = 20

    fieldsets = (
        ('Academic Period Information', {
            'fields': ('name', 'start_date', 'end_date', 'description', 'status'),
        }),
        ('Timestamps', {
            'fields': ('created', 'modified'),
        }),
    )

    readonly_fields = ('created', 'modified')

admin.site.register(AcademicPeriodModel, AcademicPeriodModelAdmin)
