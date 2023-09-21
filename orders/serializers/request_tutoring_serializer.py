from rest_framework import serializers

from general.serializers import SubjectSerializer
from orders.models import RequesttutoringModel


class RequestTutoringSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(many=False, read_only=True)
    subject_id = serializers.IntegerField(required=True, write_only=True)
    career = CareerSerializer(many=False, read_only=True)
    career_id = serializers.IntegerField(required=True, write_only=True)
    user = UserSerializer(many=False, read_only=True)
    user_id = serializers.IntegerField(required=True, write_only=True)
    user_verified = UserSerializer(many=False, read_only=True)
    user_verified_id = serializers.IntegerField(required=True, write_only=True)
    class Meta:
        model = RequesttutoringModel
        fields = (
            'id',
            'request_number',
            'reason'
            'subject',
            'subject_id'
            'user',
            'user_id'
            'career',
            'career_id'
            'user_verified',
            'user_verified_id'
            'comment',
            'status',
            'created',
            'modified',
        )
        read_only_fields = ('id', 'created', 'modified',)



