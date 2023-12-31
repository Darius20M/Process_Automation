from rest_framework import serializers

from accounts.serializers import TeacherSerializer
from catalog.models import ClassModel, ScheduleClassModel
from catalog.serializers import ClassSerializer
from general.serializers import SubjectSerializer, AcademicPeriodSerializer, ClassroomSerializer


class ScheduleClassSerializer(serializers.ModelSerializer):
    """_class = ClassSerializer(many=False, read_only=True)
    _class_id = serializers.IntegerField(required=True, write_only=True)"""
    classroom = ClassroomSerializer(many=False, read_only=True)
    classroom_id = serializers.IntegerField(required=True, write_only=True)

    class Meta:
        model = ScheduleClassModel
        fields = (
            'id',
            'classroom',
            'classroom_id',
            'day',
            'h_start',
            'h_end',
            'description',
            'created',
            'modified',
        )
        read_only_fields = ('id', 'created', 'modified',)


