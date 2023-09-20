from rest_framework import serializers

from general.models import PensumModel
from general.serializers.school_serializer import SchoolSerializer


class PensumSerializer(serializers.ModelSerializer):
    school = SchoolSerializer(many=False, read_only=True)
    school_id = serializers.IntegerField(required=True, write_only=True)
    class Meta:
        model = PensumModel
        fields = (
            'id',
            'name',
            'description',
            'school',
            'school_id',
            'start_year',
            'end_year',
            'total_credits',
            'total_hours',
            'total_hours_p',
            'total_hours_t',
            'total_subject',
            'version',
            'status',
            'created',
            'modified',
        )
        read_only_fields = ('id', 'created', 'modified',)
