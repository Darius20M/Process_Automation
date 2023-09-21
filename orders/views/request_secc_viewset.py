from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from orders.models import RequestSeccModel
from orders.serializers import  RequestSecSerializer

class  RequestSeccViewSet(ModelViewSet):
    permission_classes = (
        IsAuthenticated,
    )
    serializer_class = RequestSecSerializer
    queryset = RequestSeccModel.objects.all()
    #filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter,)
    #filterset_fields = ('director_id',)
    #ordering_fields = ('first_name', 'last_name', 'created', 'modified', 'id',)
    #search_fields = ('first_name', 'last_name', 'director_id',)
