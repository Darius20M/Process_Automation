from rest_framework import serializers

from security.models import NotificationModel
from security.serializers.user_serializer import UserSerializer


class NotificationSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    user_id = serializers.IntegerField(required=True)

    class Meta:
        model = NotificationModel
        fields = (
            'id', 'user', 'user_id','level', 'title', 'message', 'unread', 'created', 'modified',
        )
        read_only_fields = ('id', 'created', 'modified',)
