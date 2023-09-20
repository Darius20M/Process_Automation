from rest_framework import serializers

from accounts.serializers import DirectorSerializer
from general.models import SchoolModel
from general.serializers.faculty_serializer import FacultySerializer


class SchoolSerializer(serializers.ModelSerializer):
    director = DirectorSerializer(many=False, read_only=True)
    director_id = serializers.IntegerField(required=True, write_only=True)
    faculty = FacultySerializer(many=False, read_only=True)
    faculty_id = serializers.IntegerField(required=True, write_only=True)
    class Meta:
        model = SchoolModel
        fields = (
            'id',
            'name',
            'director',
            'director_id',
            'faculty',
            'faculty_id',
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
