from django.contrib import admin
from catalog.models import ClassModel

class ClassModelAdmin(admin.ModelAdmin):
    list_display = ('subject', 'teacher', 'period', 'secc', 'description', 'status', 'created', 'modified')
    list_filter = ('status', 'period__name')
    search_fields = ('subject__name', 'teacher__first_name', 'teacher__last_name', 'secc', 'description')
    list_per_page = 20

    fieldsets = (
        ('Class Information', {
            'fields': ('subject', 'teacher', 'period', 'secc', 'description', 'status'),
        }),
        ('Timestamps', {
            'fields': ('created', 'modified'),
        }),
    )

    readonly_fields = ('created', 'modified')

admin.site.register(ClassModel, ClassModelAdmin)
