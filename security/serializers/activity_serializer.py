from rest_framework import serializers

from security.models import ActivityModel
from security.serializers.user_serializer import UserSerializer


class ActivitySerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    user_id = serializers.IntegerField(required=True)

    class Meta:
        model = ActivityModel
        fields = (
            'id', 'user', 'user_id', 'activity_text', 'level', 'created', 'modified',
        )
        read_only_fields = ('id', 'created', 'modified',)
