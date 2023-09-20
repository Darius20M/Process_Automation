#from django_filters import OrderingFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from accounts.models import RoleModel
from accounts.serializers import RoleSerializer

class RoleViewSet(ModelViewSet):
    permission_classes = (
        IsAuthenticated,
    )
    serializer_class = RoleSerializer
    queryset = RoleModel.objects.all()
    #filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter,)
    filterset_fields = ('is_enabled', 'code',)
    ordering_fields = ('name', 'code', 'created', 'modified', 'id',)
    search_fields = ('name', 'code',)
