from rest_framework import serializers


class GenerateRequestTutoringSerializer(serializers.Serializer):
    subject_id = serializers.IntegerField(required=True)
