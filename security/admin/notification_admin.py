from django.contrib import admin
from orders.models import RequestSeccModel
from security.models import NotificationModel


class NotificationModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'level', 'message','unread','created', 'modified')
    list_filter = ('user', 'level', 'created', 'modified')
    search_fields = ('user__username', 'activity_text')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'modified')
    list_per_page = 20

    fieldsets = (
        ('Request Information', {
            'fields': ('user', 'title', 'level','message'),
        }),
        ('Timestamps', {
            'fields': ('created', 'modified'),
        }),
    )
admin.site.register(NotificationModel, NotificationModelAdmin)
