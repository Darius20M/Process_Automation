from django.urls import re_path
from rest_framework.routers import DefaultRouter

from general.views import AcademicPeriodViewSet,CareerViewSet,ClassroomViewSet,FacultyViewSet,PensumSubjectViewSet,PensumViewSet,SubjectViewSet,SchoolViewSet

router = DefaultRouter()
router.register(r'academic_period', AcademicPeriodViewSet)
router.register(r'career', CareerViewSet)
router.register(r'classroom', ClassroomViewSet)
router.register(r'faculty', FacultyViewSet)
router.register(r'pensum', PensumViewSet)
router.register(r'pensum_subject', PensumSubjectViewSet)
router.register(r'school', SchoolViewSet)
router.register(r'subject', SubjectViewSet)

urlpatterns = []

urlpatterns += router.urls
