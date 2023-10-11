from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from catalog.models import ClassModel, CareerStudentModel, ScheduleClassModel, ScheduleStudentModel
from catalog.serializers import ClassSerializer, CareerStudentSerializer, ScheduleClassSerializer, \
    ScheduleStudentSerializer


class ScheduleStudentViewSet(ModelViewSet):
    permission_classes = (
        IsAuthenticated,
    )
    serializer_class = ScheduleStudentSerializer
    queryset = ScheduleStudentModel.objects.all()

