from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User

from accounts.models import StudentProfileModel
from general.models import SubjectModel, AcademicPeriodModel
from orders.handlers import generate_request_tutoring_handler
from orders.serializers import GenerateRequestTutoringSerializer, RequestTutoringSerializer


class GenerateRequestTutoringViewSet(APIView):
    permission_classes = (
        IsAuthenticated,
    )

    def _get_subject(self, subject_id) -> SubjectModel:
        try:
            subject = SubjectModel.objects.get(id=subject_id)
        except SubjectModel.DoesNotExist:
            raise ValueError("This subject does not exist")
        return subject

    def _get_period(self, period_id) -> AcademicPeriodModel:
        try:
            period = AcademicPeriodModel.objects.get(id=period_id)
        except AcademicPeriodModel.DoesNotExist:
            raise ValueError("This period does not exist")
        return period

    def _get_student(self, user) -> StudentProfileModel:
        try:
            student = StudentProfileModel.objects.get(user=user)
        except StudentProfileModel.DoesNotExist:
            raise ValueError("This student does not exist")
        return student

    def post(self, request, pk=None, format=None):
        serializer = GenerateRequestTutoringSerializer(data=request.data)
        if serializer.is_valid():

            subject = self._get_subject(subject_id=serializer.validated_data.get('subject_id'))
            shift = serializer.validated_data.get('shift')
            period = self._get_period(period_id=serializer.validated_data.get('period_id'))
            student = self._get_student(user=request.user)

            request_verify = generate_request_tutoring_handler(
                subject=subject,
                shift=shift,
                student=student,
                period = period,
                user=request.user
            )

            return Response(RequestTutoringSerializer(instance=request_verify, many=False).data,
                            status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
