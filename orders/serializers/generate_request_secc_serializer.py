from rest_framework import serializers

class GenerateRequestSeccSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(required=True)