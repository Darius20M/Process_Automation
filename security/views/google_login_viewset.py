import json
import requests
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from security.serializers.user_serializer import UserSerializer


class GoogleLoginView(APIView):
    def post(self, request):
        payload = {'access_token': request.data.get("token")}  # validate the token
        r = requests.get('https://www.googleapis.com/oauth2/v2/userinfo', params=payload)
        data = json.loads(r.text)

        if 'error' in data:
            content = {'message': 'wrong google token / this google token is already expired.'}
            return Response(content)

        # create user if not exist
        try:
            user = User.objects.get(email=data.get('email'))
        except User.DoesNotExist:
            user = User()
            user.username = data.get('email')
            user.first_name = data.get('given_name')
            user.last_name = data.get('family_name')
            # provider random default password
            user.password = make_password(BaseUserManager().make_random_password())
            user.email = data.get('email')
            user.save()

        token = RefreshToken.for_user(user)  # generate token without username & password
        response = {}
        response['user'] = UserSerializer(instance=user).data
        response['access_token'] = str(token.access_token)
        response['refresh_token'] = str(token)
        return Response(response, status=status.HTTP_200_OK)