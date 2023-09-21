from rest_framework import serializers

from accounts.serializers.user_list_serializer import UserListSerializer
from accounts.serializers.role_serializer import RoleSerializer

from accounts.models import StudentProfileModel


class StudentProfileSerializer(serializers.ModelSerializer):
    role = RoleSerializer(many=False, read_only=True)
    role_id = serializers.IntegerField(required=True, write_only=True)
    user = UserListSerializer(many=False, read_only=True)
    user_id = serializers.IntegerField(required=True, write_only=True)
    class Meta:
        model = StudentProfileModel
        fields = (
            'id',
            'user',
            'user_id',
            'first_name',
            'last_name',
            'student_id',
            'identification_number',
            'enrollment_date',
            'enrollment_status',
            'date_of_birth',
            'gender',
            'address',
            'contact_phone',
            'email',
            'role',
            'role_id',
            'created',
            'modified',
        )
        read_only_fields = ('id', 'student_id','identification_number', 'created', 'modified',)



