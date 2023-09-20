from rest_framework import serializers

from accounts.models import RoleModel


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleModel
        fields = (
            'id',
            'code',
            'name',
            'is_enabled',
            'about',
            'created',
            'modified',
        )
        read_only_fields = ('id', 'created', 'modified',)