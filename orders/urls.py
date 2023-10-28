from django.urls import re_path
from rest_framework.routers import DefaultRouter

from orders.views import RequestSeccViewSet, RequestTutoringViewSet, GenerateRequestSeccViewSet, \
    GenerateRequestTutoringViewSet

router = DefaultRouter()
router.register(r'request_secc', RequestSeccViewSet)
router.register(r'request_tutoring', RequestTutoringViewSet)


urlpatterns = [
    re_path(r'^generate_request_tutoring/', GenerateRequestTutoringViewSet.as_view(), name='generate_request_tutoring'),
   re_path(r'^generate_request_secc/', GenerateRequestSeccViewSet.as_view(), name='generate_request_secc'),

]

urlpatterns += router.urls
