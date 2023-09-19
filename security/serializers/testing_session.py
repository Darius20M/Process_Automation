from abc import ABC

from rest_framework import serializers


class TestingSerializer(serializers.Serializer):
    token = serializers.CharField()

