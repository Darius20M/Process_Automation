from django.contrib import admin

from django.db import models  # Agrega esta importación
from catalog.models import ClassModel, ScheduleClassModel


class ScheduleClassInline(admin.TabularInline):
    model = ScheduleClassModel
    suit_classes = 'suit-tab suit-tab-cities'
    extra = 1
class ClassModelAdmin(admin.ModelAdmin):
    inlines = (ScheduleClassInline,)

    list_display = ('subject', 'teacher', 'period', 'secc', 'description', 'status', 'created', 'modified')
    list_filter = ('status', 'period__name')
    search_fields = ('subject__name', 'teacher__first_name', 'teacher__last_name', 'secc', 'description')
    list_per_page = 20
    list_editable = ('description', 'status')



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
