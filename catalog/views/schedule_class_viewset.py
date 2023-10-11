from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from catalog.models import ClassModel, CareerStudentModel, ScheduleClassModel
from catalog.serializers import ClassSerializer, CareerStudentSerializer, ScheduleClassSerializer


class ScheduleClassViewSet(ModelViewSet):
    permission_classes = (
        IsAuthenticated,
    )
    serializer_class = ScheduleClassSerializer
    queryset = ScheduleClassModel.objects.all()

