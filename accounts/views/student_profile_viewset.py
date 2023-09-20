from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from accounts.models import StudentProfileModel
from accounts.serializers import StudentProfileSerializer

class StudentProfileViewSet(ModelViewSet):
    permission_classes = (
        IsAuthenticated,
    )
    serializer_class = StudentProfileSerializer
    queryset = StudentProfileModel.objects.all()
    #filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter,)
    filterset_fields = ('student_id',)
    ordering_fields = ('first_name','last_name', 'created', 'modified', 'id',)
    search_fields = ('first_name', 'last_name', 'student_id',)
