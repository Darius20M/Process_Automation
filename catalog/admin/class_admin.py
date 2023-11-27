from django.contrib import admin

from django.db import models  # Agrega esta importación
from catalog.models import ClassModel, ScheduleClassModel, ScheduleStudentModel, SubjectStudentModel


class ScheduleClassInline(admin.TabularInline):
    model = ScheduleClassModel
    suit_classes = 'suit-tab suit-tab-cities'
    extra = 1


class ClassModelAdmin(admin.ModelAdmin):
    inlines = (ScheduleClassInline,)

    list_display = ('subject', 'student','is_tutoring_now', 'teacher', 'period', 'secc', 'description', 'status', 'created', 'modified')
    list_filter = ('status','subject','period','student__student_id')
    search_fields = ('subject__name', 'teacher__first_name', 'teacher__last_name', 'secc', 'description')
    list_per_page = 20
    list_editable = ('status',)

    fieldsets = (
        ('Class Information', {
            'fields': ('subject','is_tutoring_now', 'student', 'teacher', 'period', 'secc', 'description', 'status'),
        }),
        ('Timestamps', {
            'fields': ('created', 'modified'),
        }),
    )

    readonly_fields = ('created', 'modified')

    def save_model(self, request, obj, form, change):
        subject_student = SubjectStudentModel.objects.get(student=obj.student, subject=obj.subject)
        subject_student.status = 'ongoing'
        subject_student.save()
        obj.save()


admin.site.register(ClassModel, ClassModelAdmin)
