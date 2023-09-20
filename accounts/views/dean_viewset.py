#from django_filters import OrderingFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from accounts.models import DeanModel
from accounts.serializers import DeanSerializer

class DeanViewSet(ModelViewSet):
    permission_classes = (
        IsAuthenticated,
    )
    serializer_class = DeanSerializer
    queryset = DeanModel.objects.all()
    #filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter,)
    filterset_fields = ('director_id',)
    ordering_fields = ('first_name', 'last_name', 'created', 'modified', 'id',)
    search_fields = ('first_name', 'last_name', 'director_id',)
