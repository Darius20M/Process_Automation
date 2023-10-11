from django.contrib import admin
from catalog.models import CareerStudentModel

class CareerStudentModelAdmin(admin.ModelAdmin):
    list_display = ('student', 'career', 'description', 'status', 'created', 'modified')
    list_filter = ('status',)
    search_fields = ('student__first_name', 'student__last_name', 'career__name', 'description')
    list_per_page = 20

    fieldsets = (
        ('Career Student Information', {
            'fields': ('student', 'career', 'description', 'status'),
        }),
        ('Timestamps', {
            'fields': ('created', 'modified'),
        }),
    )

    readonly_fields = ('created', 'modified')

admin.site.register(CareerStudentModel, CareerStudentModelAdmin)
