from django.urls import re_path
from rest_framework.routers import DefaultRouter

from orders.views import RequestSeccViewSet, RequestTutoringViewSet

router = DefaultRouter()
router.register(r'request_secc', RequestSeccViewSet)
router.register(r'request_tutoring', RequestTutoringViewSet)


urlpatterns = []

urlpatterns += router.urls
