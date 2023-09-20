from rest_framework import serializers

from accounts.serializers import DeanSerializer
from general.models import FacultyModel


class FacultySerializer(serializers.ModelSerializer):
    dean = DeanSerializer(many=False, read_only=True)
    dean_id = serializers.IntegerField(required=True, write_only=True)
    class Meta:
        model = FacultyModel
        fields = (
            'id',
            'name',
            'dean',
            'dean_id',
            'description',
            'established_date',
            'website',
            'contact_email',
            'phone_number',
            'location',
            'created',
            'modified',
        )
        read_only_fields = ('id', 'created', 'modified',)
