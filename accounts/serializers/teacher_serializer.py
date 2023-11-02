from rest_framework import serializers

from accounts.serializers.user_list_serializer import UserListSerializer
from accounts.serializers.role_serializer import RoleSerializer

from accounts.models import DeanModel, TeacherModel
from general.serializers import SchoolSerializer


class TeacherSerializer(serializers.ModelSerializer):
    role = RoleSerializer(many=False, read_only=True)
    role_id = serializers.IntegerField(required=True, write_only=True)

    school = SchoolSerializer(many=False, read_only=True)
    school_id = serializers.IntegerField(required=True, write_only=True)
    class Meta:
        model = TeacherModel
        fields = (
            'id',
            'first_name',
            'last_name',
            'teacher_id',
            'identification_number',
            'enrollment_date',
            'enrollment_status',
            'date_of_birth',
            'gender',
            'address',
            'contact_phone',
            'email',
            'school',
            'school_id',
            'role',
            'role_id',
            'created',
            'modified',
        )
        read_only_fields = ('id', 'teacher_id','identification_number', 'created', 'modified',)



