from rest_framework import serializers
from general.models import CareerModel
from general.serializers.school_serializer import SchoolSerializer
from general.serializers.pensum_serializer import PensumSerializer


class CareerSerializer(serializers.ModelSerializer):
    pensum = PensumSerializer(many=False, read_only=True)
    pensum_id = serializers.IntegerField(required=True, write_only=True)
    school = SchoolSerializer(many=False, read_only=True)
    school_id = serializers.IntegerField(required=True, write_only=True)
    class Meta:
        model = CareerModel
        fields = (
            'id',
            'name',
            'degree',
            'description',
            'duration_in_semesters',
            'pensum_id',
            'pensum',
            'school',
            'school_id',
            'status',
            'created',
            'modified',
        )
        read_only_fields = ('id', 'created', 'modified',)

