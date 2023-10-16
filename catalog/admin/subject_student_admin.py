from django.contrib import admin
from catalog.models import SubjectStudentModel

class SubjectStudentModelAdmin(admin.ModelAdmin):
    list_display = ('subject', 'student', 'status', 'created', 'modified')
    list_filter = ('status', 'subject__code', 'student__student_id','student__user__first_name', 'student__user__last_name')
    search_fields = ('subject__code', 'student__user__first_name', 'student__user__last_name', 'status')
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


admin.site.register(SubjectStudentModel, SubjectStudentModelAdmin)
