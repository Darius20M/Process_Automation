from django.contrib import admin
from catalog.models import ScheduleStudentModel

class ScheduleStudentModelAdmin(admin.ModelAdmin):
    list_display = ('student', 'schedule', 'status', 'created', 'modified')
    list_filter = ('status', 'student__user__first_name', 'student__user__last_name', 'schedule__classroom__code', 'schedule__day')
    search_fields = ('student__user__first_name', 'student__user__last_name', 'schedule__classroom__code', 'status')
    list_per_page = 20

    fieldsets = (
        ('Schedule Student Information', {
            'fields': ('student', 'schedule', 'status'),
        }),
        ('Timestamps', {
            'fields': ('created', 'modified'),
        }),
    )

    readonly_fields = ('created', 'modified')

admin.site.register(ScheduleStudentModel, ScheduleStudentModelAdmin)
