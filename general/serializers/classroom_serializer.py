from rest_framework import serializers
from general.models import ClassroomModel


class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassroomModel
        fields = (
            'id',
            'code',
            'capacity',
            'building',
            'floor',
            'status',
            'created',
            'modified',
        )
        read_only_fields = ('id', 'created', 'modified',)
