from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from orders.serializers import GenerateRequestSeccSerializer


class GenerateRequestSeccViewSet(APIView):
    permission_classes = (
        IsAuthenticated,

    )
    def post(self, request, pk=None, format=None):
        serializer = GenerateRequestSeccSerializer(data=request.data)
        if serializer.is_valid():



            """create_activity_handler(
                application=request.application,
                user=request.user,
                level='INFO',
                activity_text=_('You have completed the practice verification process.')
            )
            request_verify = generate_request_verify(request, practice_obj)"""

            #return Response(RequestVerificationSerializer(instance=request_verify, many=False).data, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)