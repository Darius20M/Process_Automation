from rest_framework import serializers

from accounts.serializers import StudentProfileSerializer
from catalog.models import CareerStudentModel


class CareerStudentSerializer(serializers.ModelSerializer):
    student = StudentProfileSerializer(many=False, read_only=True)
    student_id = serializers.IntegerField(required=True, write_only=True)
    career = CareerSerializer(many=False, read_only=True)
    career_id = serializers.IntegerField()
    class Meta:
        model = CareerStudentModel
        fields = (
            'id',
            'student',
            'student_id',
            'career',
            'career_id',
            'description',
            'created',
            'modified',
        )
        read_only_fields = ('id', 'created', 'modified',)


