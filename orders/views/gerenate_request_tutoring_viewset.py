from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from general.models import SubjectModel
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

    def post(self, request, pk=None, format=None):
        serializer = GenerateRequestTutoringSerializer(data=request.data)
        if serializer.is_valid():

            subject = self._get_subject(subject_id=serializer.validated_data.get('subject_id'))
            request_verify = generate_request_tutoring_handler(
                subject=subject
            )

            return Response(RequestTutoringSerializer(instance=request_verify, many=False).data,
                            status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
