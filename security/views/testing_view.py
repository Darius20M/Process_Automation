from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from security.serializers import TestingSerializer


class TestingView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk=None, format=None):
        serializer = TestingSerializer(data=request.data)
        if serializer.is_valid():
            print('h')
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)