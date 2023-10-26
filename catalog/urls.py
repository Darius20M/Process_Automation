from django.urls import re_path
from rest_framework.routers import DefaultRouter

from catalog.views.career_student_viewset import CareerStudentViewSet
from catalog.views.class_viewset import ClassViewSet
from catalog.views.schedule_class_viewset import ScheduleClassViewSet
from catalog.views.schedule_student_viewset import ScheduleStudentViewSet
from catalog.views.subject_student_viewset import SubjectStudentViewSet

router = DefaultRouter()
router.register(r'subject_student', SubjectStudentViewSet)
router.register(r'class', ClassViewSet)
router.register(r'schedule_class', ScheduleClassViewSet)
router.register(r'schedule_student', ScheduleStudentViewSet)
router.register(r'career_student', CareerStudentViewSet)




urlpatterns = []

urlpatterns += router.urls
