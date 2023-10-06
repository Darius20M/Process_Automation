from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from catalog.models import ClassModel
from catalog.serializers import ClassSerializer


class ClassViewSet(ModelViewSet):
    permission_classes = (
        IsAuthenticated,
    )
    serializer_class = ClassSerializer
    queryset = ClassModel.objects.all()

