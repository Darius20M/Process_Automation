from rest_framework import serializers

from accounts.serializers import TeacherSerializer
from catalog.models import ClassModel
from general.serializers import SubjectSerializer, AcademicPeriodSerializer


class ClassSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(many=False, read_only=True)
    subject_id = serializers.IntegerField(required=True, write_only=True)
    teacher = TeacherSerializer(many=False, read_only=True)
    teacher_id = serializers.IntegerField(required=True, write_only=True)
    period = AcademicPeriodSerializer(many=False, read_only=True)
    period_id = serializers.IntegerField()
    # student = StudentProfileSerializer(many=False, read_only=True)
    student_id = serializers.IntegerField(required=True, write_only=True)
    class Meta:
        model = ClassModel
        fields = (
            'id',
            'subject',
            'subject_id',
            'student',
            'student_id',
            'teacher',
            'teacher_id',
            'period',
            'period_id',
            'is_tutoring_now',
            'description',
            'created',
            'modified',
        )
        read_only_fields = ('id', 'created', 'modified',)

    def to_representation(self, instance):
        from catalog.serializers.schedule_class_serializer import ScheduleClassSerializer

        # Asegúrate de utilizar el nombre relacionado correcto
        schedule_instances = instance.schedule.all()  # Usa el nombre relacionado, por ejemplo, 'schedule'
        representation = super().to_representation(instance)
        representation['schedule'] = ScheduleClassSerializer(schedule_instances, many=True).data
        return representation


