from django.contrib import admin
from general.models import SubjectModel, UniversityRuleModel


class UniversityRuleModelAdmin(admin.ModelAdmin):
    list_display = (
    'id', 'min_of_credit_tutoring', 'max_of_sub_tutoring', 'max_student_become_special', 'min_student_secc', 'created',
    'modified')
    list_filter = ('min_of_credit_tutoring', 'max_of_sub_tutoring', 'max_student_become_special', 'min_student_secc')
    search_fields = ('min_of_credit_tutoring', 'max_of_sub_tutoring', 'max_student_become_special', 'min_student_secc')

    fieldsets = (
        ('Basic Information', {
            'fields': (
            'min_of_credit_tutoring', 'max_of_sub_tutoring', 'max_student_become_special', 'min_student_secc')
        }),
        ('Date Information', {
            'fields': ('created', 'modified'),
            'classes': ('collapse',),
        }),
    )

    readonly_fields = ('created', 'modified')


admin.site.register(UniversityRuleModel, UniversityRuleModelAdmin)


