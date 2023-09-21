from rest_framework import serializers

class GenerateRequestTutoringSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(required=True)


