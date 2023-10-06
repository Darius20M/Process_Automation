from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from catalog.models import ClassModel, CareerStudentModel, ScheduleClassModel, ScheduleStudentModel, SubjectStudentModel
from catalog.serializers.subject_student_serializer import SubjectStudentSerializer


class SubjectStudentViewSet(ModelViewSet):
    permission_classes = (
        IsAuthenticated,
    )
    serializer_class = SubjectStudentSerializer
    queryset = SubjectStudentModel.objects.all()

