from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from security.models import ActivityModel
from security.serializers import ActivitySerializer


class ActivityViewSet(ModelViewSet):
    permission_classes = (
        IsAuthenticated,
    )
    serializer_class = ActivitySerializer
    queryset = ActivityModel.objects.all()
    ordering_fields = ('id',)
    filterset_fields = {
        'user': ['exact'],
        'created': ['gte', 'lte', 'exact', 'gt', 'lt'],
    }
    search_fields = ('title', 'user__first_name', 'user__username', 'user__email', 'user__last_name', 'message',)