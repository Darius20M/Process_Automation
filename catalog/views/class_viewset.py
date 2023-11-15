from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from catalog.filter import StudentFilter
from catalog.models import ClassModel
from catalog.serializers import ClassSerializer


class ClassViewSet(ModelViewSet):
    permission_classes = (
       IsAuthenticated,
    )
    serializer_class = ClassSerializer
    queryset = ClassModel.objects.all()
    filter_backends = (StudentFilter,DjangoFilterBackend, SearchFilter, OrderingFilter,)
    filterset_fields = ('student_id', 'subject_id', 'subject__is_tutoring','is_tutoring_now', 'status')


