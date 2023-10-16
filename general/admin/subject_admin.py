from django.contrib import admin
from general.models import SubjectModel


class SubjectModelAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'is_tutoring','credits', 'to_hours', 'p_hours', 't_hours', 'status')
    list_filter = ('status','is_tutoring')
    search_fields = ('code', 'name')
    list_per_page = 20

    fieldsets = (
        ('Subject Information', {
            'fields': ('code', 'name'),
        }),
        ('Other Information', {
            'fields': ('credits', 'to_hours', 'p_hours', 't_hours', 'is_tutoring', 'status'),
        }),
    )

    readonly_fields = ('created', 'modified')


admin.site.register(SubjectModel, SubjectModelAdmin)
