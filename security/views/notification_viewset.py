from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from security.models import NotificationModel
from security.serializers import NotificationSerializer


class NotificationViewSet(ModelViewSet):
    permission_classes = (
        IsAuthenticated,
    )
    serializer_class = NotificationSerializer
    queryset = NotificationModel.objects.all()
    ordering_fields = ('id', 'created')
    filterset_fields = ('user','request_n', 'level', 'unread', 'created',)
    search_fields = ('title', 'user__first_name', 'user__username', 'user__email', 'user__last_name', 'message',)