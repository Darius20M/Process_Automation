from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from catalog.models import ClassModel, CareerStudentModel
from catalog.serializers import ClassSerializer, CareerStudentSerializer


class CareerStudentViewSet(ModelViewSet):
    permission_classes = (
        IsAuthenticated,
    )
    serializer_class = CareerStudentSerializer
    queryset = CareerStudentModel.objects.all()

