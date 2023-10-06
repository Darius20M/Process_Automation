from django.contrib import admin
from general.models import ClassroomModel

class ClassroomModelAdmin(admin.ModelAdmin):
    list_display = ('code', 'capacity', 'building', 'floor', 'status', 'created', 'modified')
    list_filter = ('status', 'building')
    search_fields = ('code', 'building')
    list_per_page = 20

    fieldsets = (
        ('Classroom Information', {
            'fields': ('code', 'capacity', 'building', 'floor', 'status'),
        }),
        ('Timestamps', {
            'fields': ('created', 'modified'),
        }),
    )

    readonly_fields = ('created', 'modified')

admin.site.register(ClassroomModel, ClassroomModelAdmin)
