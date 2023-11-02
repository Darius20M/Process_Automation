from django.db.models import Q
from rest_framework.filters import BaseFilterBackend

class StudentProfileFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if request.user.is_staff or request.user.is_superuser:
            return queryset
        else:
            queryset = queryset.filter(
                Q(user=request.user)
            )

            return queryset