from django.urls import re_path
from rest_framework.routers import DefaultRouter

from accounts.views import DeanViewSet, DirectorViewSet, StudentProfileViewSet, TeacherViewSet, RoleViewSet

router = DefaultRouter()
router.register(r'dean', DeanViewSet)
router.register(r'director', DirectorViewSet)
router.register(r'student', StudentProfileViewSet)
router.register(r'teacher', TeacherViewSet)
router.register(r'role', RoleViewSet)

urlpatterns = []

urlpatterns += router.urls
