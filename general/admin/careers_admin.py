from django.contrib import admin
from general.models import CareerModel

class CareerModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'pensum', 'school', 'degree', 'duration_in_semesters', 'status', 'created', 'modified')
    list_filter = ('status', 'school')
    search_fields = ('name', 'description', 'degree')
    list_per_page = 20

    fieldsets = (
        ('Career Information', {
            'fields': ('name', 'pensum', 'school', 'degree', 'duration_in_semesters', 'description', 'status'),
        }),
        ('Timestamps', {
            'fields': ('created', 'modified'),
        }),
    )

    readonly_fields = ('created', 'modified')

admin.site.register(CareerModel, CareerModelAdmin)
