from django.urls import re_path
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
#router.register(r'subject_student_serializer', Subject)


urlpatterns = []

urlpatterns += router.urls
