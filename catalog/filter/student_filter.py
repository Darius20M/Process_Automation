from django.db.models import Q
from rest_framework.filters import BaseFilterBackend

class StudentFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if request.user.is_staff or request.user.is_superuser:
            return queryset
        else:
            queryset = queryset.filter(
                Q(student__user=request.user)
            )

            return queryset