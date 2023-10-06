from django.contrib import admin
from general.models import PensumSubjectModel

class PensumSubjectModelAdmin(admin.ModelAdmin):
    list_display = ('subject', 'pensum', 'prerequisites', 'period', 'status', 'created', 'modified')
    list_filter = ('status',)
    search_fields = ('subject__name', 'pensum__name', 'description')
    list_per_page = 20

    fieldsets = (
        ('Pensum Subject Information', {
            'fields': ('subject', 'pensum', 'prerequisites', 'period', 'description', 'status'),
        }),
        ('Timestamps', {
            'fields': ('created', 'modified'),
        }),
    )

    readonly_fields = ('created', 'modified')

admin.site.register(PensumSubjectModel, PensumSubjectModelAdmin)
