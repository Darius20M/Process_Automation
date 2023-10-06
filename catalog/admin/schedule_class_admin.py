from django.contrib import admin
from catalog.models import ScheduleClassModel

class ScheduleClassModelAdmin(admin.ModelAdmin):
    list_display = ('_class', 'classroom', 'day', 'h_start', 'h_end', 'description', 'status', 'created', 'modified')
    list_filter = ('status', 'day', '_class__subject__name', '_class__teacher__first_name', '_class__teacher__last_name')
    search_fields = ('_class__subject__name', '_class__teacher__first_name', '_class__teacher__last_name', 'classroom__code', 'day', 'description')
    list_per_page = 20

    fieldsets = (
        ('Schedule Information', {
            'fields': ('_class', 'classroom', 'day', 'h_start', 'h_end', 'description', 'status'),
        }),
        ('Timestamps', {
            'fields': ('created', 'modified'),
        }),
    )

    readonly_fields = ('created', 'modified')

admin.site.register(ScheduleClassModel, ScheduleClassModelAdmin)
