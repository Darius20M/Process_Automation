from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from orders.models import RequesttutoringModel
from orders.serializers import  RequestSeccSerializer

class  RequestTutoringViewSet(ModelViewSet):
    permission_classes = (
        IsAuthenticated,
    )
    serializer_class = RequestSeccSerializer
    queryset = RequesttutoringModel.objects.all()
    #filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter,)
    #filterset_fields = ('director_id',)
    #ordering_fields = ('first_name', 'last_name', 'created', 'modified', 'id',)
    #search_fields = ('first_name', 'last_name', 'director_id',)
