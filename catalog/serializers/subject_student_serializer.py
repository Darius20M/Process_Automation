from rest_framework import serializers

from accounts.serializers import TeacherSerializer, StudentProfileSerializer
from catalog.models import ClassModel
from catalog.models.subject_student_model import SubjectStudentModel
from general.serializers import SubjectSerializer, AcademicPeriodSerializer


class SubjectStudentSerializer(serializers.ModelSerializer):
    student = StudentProfileSerializer(many=False, read_only=True)
    student_id = serializers.IntegerField(required=True, write_only=True)
    subject = SubjectSerializer(many=False, read_only=True)
    subject_id = serializers.IntegerField(required=True, write_only=True)
    class Meta:
        model = SubjectStudentModel
        fields = (
            'id',
            'student',
            'student_id',
            'subject',
            'subject_id',
            'created',
            'modified',
        )
        read_only_fields = ('id', 'created', 'modified',)


