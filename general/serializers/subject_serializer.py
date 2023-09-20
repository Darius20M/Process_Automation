from rest_framework import serializers

from general.models import SubjectModel

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectModel
        fields = (
            'id',
            'code',
            'name',
            'credits',
            'to_hours',
            'p_hours',
            't_hours',
            'status',
        )

        read_only_fields = ('id', 'created', 'modified',)
