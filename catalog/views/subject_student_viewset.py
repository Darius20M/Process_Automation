from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter, SearchFilter

from catalog.filter import StudentFilter
from catalog.models import ClassModel, CareerStudentModel, ScheduleClassModel, ScheduleStudentModel, SubjectStudentModel
from catalog.serializers.subject_student_serializer import SubjectStudentSerializer


class SubjectStudentViewSet(ModelViewSet):
    """permission_classes = (
        IsAuthenticated,
    )"""
    serializer_class = SubjectStudentSerializer
    queryset = SubjectStudentModel.objects.all()
    filter_backends = (StudentFilter,DjangoFilterBackend, SearchFilter, OrderingFilter,)
    filterset_fields = ('student_id', 'subject_id', 'subject__is_tutoring', 'status')
    ordering_fields = ()
    search_fields = ()



