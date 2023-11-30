from rest_framework import serializers


class RequestCrendentialSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)

