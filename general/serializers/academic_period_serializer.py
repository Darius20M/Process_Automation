from rest_framework import serializers
from general.models import AcademicPeriodModel


class AcademicPeriodSerializer(serializers.ModelSerializer):

    class Meta:
        model = AcademicPeriodModel
        fields = (
            'id',
            'name',
            'start_date',
            'end_date',
            'status',
            'created',
            'modified',
        )
        read_only_fields = ('id', 'created', 'modified',)



