from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from general.models import ClassroomModel
from general.serializers import ClassroomSerializer


class ClassroomViewSet(ModelViewSet):
    permission_classes = (
        IsAuthenticated,
    )
    serializer_class = ClassroomSerializer
    queryset = ClassroomModel.objects.all()
    filter_backends = (SearchFilter, OrderingFilter,)
    filterset_fields = ('code','capacity','building','floor','status')
    # ordering_fields = ('first_name', 'last_name', 'created', 'modified', 'id',)
    # search_fields = ('first_name', 'last_name', 'director_id',)
