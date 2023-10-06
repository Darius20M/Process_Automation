from rest_framework import serializers

from general.models import PensumSubjectModel
from general.serializers import PensumSerializer
from general.serializers.subject_serializer import SubjectSerializer

class PensumSubjectSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(many=False, read_only=True)
    subject_id = serializers.IntegerField(required=True, write_only=True)
    """prerequisites = SubjectSerializer(many=False, read_only=True)
    prerequisites_id = serializers.IntegerField(required=True, write_only=True)"""
    pensum = PensumSerializer(many=False, read_only=True)
    pensum_id = serializers.IntegerField(required=True, write_only=True)
    class Meta:
        model = PensumSubjectModel
        fields = (
            'id',
            'subject',
            'subject_id',
            'pensum',
            'pensum_id',
            'prerequisites',
            'period',
            'description',
            'status',
            'created',
            'modified',
        )
        read_only_fields = ('id', 'created', 'modified',)
