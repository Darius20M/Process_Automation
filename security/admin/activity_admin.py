from django.contrib import admin
from orders.models import RequesttutoringModel
from security.models import ActivityModel


class ActivityModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'activity_text', 'level', 'created', 'modified')
    list_filter = ('user', 'level', 'created', 'modified')
    search_fields = ('user__username', 'activity_text')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'modified')
    list_per_page = 20

    fieldsets = (
        ('Request Information', {
            'fields': ('user', 'activity_text', 'level'),
        }),
        ('Timestamps', {
            'fields': ('created', 'modified'),
        }),
    )

admin.site.register(ActivityModel, ActivityModelAdmin)
