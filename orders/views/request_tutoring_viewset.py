from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from accounts.filter import StudentProfileFilter
from orders.models import RequesttutoringModel
from orders.serializers import  RequestSecSerializer

class  RequestTutoringViewSet(ModelViewSet):
    permission_classes = (
        IsAuthenticated,
    )
    serializer_class = RequestSecSerializer
    queryset = RequesttutoringModel.objects.all()
    filter_backends = (StudentProfileFilter,DjangoFilterBackend, SearchFilter, OrderingFilter,)
    filterset_fields = ('status',)
    #ordering_fields = ('first_name', 'last_name', 'created', 'modified', 'id',)
    #search_fields = ('first_name', 'last_name', 'director_id',)
