from rest_framework import serializers

from accounts.serializers import TeacherSerializer, StudentProfileSerializer
from catalog.models import ClassModel, ScheduleStudentModel
from general.serializers import SubjectSerializer, AcademicPeriodSerializer


class ScheduleStudentSerializer(serializers.ModelSerializer):
    student = StudentProfileSerializer(many=False, read_only=True)
    student_id = serializers.IntegerField(required=True, write_only=True)
    schedule_class = ScheduleClassSerializer(many=False, read_only=True)
    schedule_class_id = serializers.IntegerField()


    class Meta:
        model = ScheduleStudentModel
        fields = (
            'id',
            'student',
            'student_id',
            'schedule_class',
            'schedule_class_id',
            'description',
            'created',
            'modified',
        )
        read_only_fields = ('id', 'created', 'modified',)


