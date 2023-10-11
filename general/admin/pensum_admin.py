from django.contrib import admin
from general.models import PensumModel, PensumSubjectModel


class PensumInline(admin.TabularInline):
    model = PensumSubjectModel
    suit_classes = 'suit-tab suit-tab-cities'
    extra = 1
class PensumModelAdmin(admin.ModelAdmin):
    inlines = (PensumInline,)

    list_display = ('name', 'school', 'start_year', 'end_year', 'total_credits', 'total_hours', 'total_hours_p', 'total_hours_t', 'total_subject', 'version', 'status')
    list_filter = ('status', 'school')
    search_fields = ('name', 'description')
    list_per_page = 20

    fieldsets = (
        ('Pensum Information', {
            'fields': (
                ('name', ),
                'school',
                ('start_year', 'end_year'),
                ('total_credits', 'total_hours'),
                ('total_hours_p', 'total_hours_t'),
                'total_subject',
                'description',
                'version',
                'status',
            ),
        }),
        ('Timestamps', {
            'fields': ('created', 'modified'),
        }),
    )

    readonly_fields = ('created', 'modified')

admin.site.register(PensumModel, PensumModelAdmin)
