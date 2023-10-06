from django.contrib import admin
from orders.models import RequesttutoringModel
from django.utils import timezone

from sequences import get_next_value
class RequesttutoringModelAdmin(admin.ModelAdmin):
    list_display = ('request_number', 'subject', 'user', 'career', 'status', 'user_verified', 'created', 'modified')
    list_filter = ('status', 'subject', 'career')
    search_fields = ('request_number', 'user__username', 'user__first_name', 'user__last_name', 'user__email')
    list_per_page = 20

    fieldsets = (
        ('Request Information', {
            'fields': ('subject', 'user', 'career', 'request_number', 'reason', 'status', 'user_verified', 'comment'),
        }),
        ('Timestamps', {
            'fields': ('created', 'modified'),
        }),
    )

    readonly_fields = ('request_number', 'created', 'modified')

    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.request_number = "RT{0}".format(get_next_value("request_tutoring", initial_value=1000))
        obj.modified = timezone.now()
        super().save_model(request, obj, form, change)

admin.site.register(RequesttutoringModel, RequesttutoringModelAdmin)
