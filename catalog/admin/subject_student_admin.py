from django.contrib import admin
from catalog.models import SubjectStudentModel

class SubjectStudentModelAdmin(admin.ModelAdmin):
    list_display = ('subject', 'student', 'status', 'created', 'modified')
    list_filter = ('status', 'subject__code', 'student__student_id','student__user__first_name', 'student__user__last_name')
    search_fields = ('subject__code', 'student__student_id','student__user__first_name', 'student__user__last_name', 'status')
    list_per_page = 20

    fieldsets = (
        ('Subject Student Information', {
            'fields': ('subject', 'student', 'status'),
        }),
        ('Timestamps', {
            'fields': ('created', 'modified'),
        }),
    )

    readonly_fields = ('created', 'modified')
    ordering = ('subject__code', 'subject__name',)
    def make_status_active(self, request, queryset):
        queryset.update(status='approved')

    def make_status_inactive(self, request, queryset):
        queryset.update(status='due')

    make_status_active.short_description = "approved subject"
    make_status_inactive.short_description = "due subject"

    actions = [make_status_active, make_status_inactive]


admin.site.register(SubjectStudentModel, SubjectStudentModelAdmin)
