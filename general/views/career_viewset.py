from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from general.models import CareerModel
from general.serializers import  CareerSerializer

class  CareerViewSet(ModelViewSet):
    permission_classes = (
        IsAuthenticated,
    )
    serializer_class = CareerSerializer
    queryset = CareerModel.objects.all()
    #filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter,)
    #filterset_fields = ('director_id',)
    #ordering_fields = ('first_name', 'last_name', 'created', 'modified', 'id',)
    #search_fields = ('first_name', 'last_name', 'director_id',)
