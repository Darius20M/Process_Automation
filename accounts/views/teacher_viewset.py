from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from accounts.models import TeacherModel
from accounts.serializers import TeacherSerializer

class TeacherViewSet(ModelViewSet):
    permission_classes = (
        IsAuthenticated,
    )
    serializer_class = TeacherSerializer
    queryset = TeacherModel.objects.all()
    #filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter,)
    filterset_fields = ('teacher_id',)
    ordering_fields = ('first_name', 'last_name', 'created', 'modified', 'id',)
    search_fields = ('first_name', 'last_name', 'teacher_id',)
