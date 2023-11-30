from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from orders.handlers import send_email_handler


class RequestCredentialViewSet(APIView):

    def post(self, request, format=None):

        email = request.data.get('email', None)

        if not email:
            return Response({'detail': 'El campo de correo electrónico es obligatorio.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'detail': 'No se encontró ningún usuario con este correo electrónico.'}, status=status.HTTP_404_NOT_FOUND)

        # Genera una nueva contraseña
        new_password = User.objects.make_random_password()

        # Establece la nueva contraseña para el usuario
        user.password = make_password(new_password)
        user.save()

        user_name=user.username
        name = "{} {}".format(user.first_name, user.last_name)


        sender_email = 'UCSD <dariusjosedelacruzhilario@gmail.com>'
        receiver_email = user.email
        subject = 'Solicitud de credenciales'
        email_template = 'user_creation_change_email.html'

        context = {
                'name':name,
                'inf': user_name,
                'pass': new_password,
        }

        html_content = render_to_string(email_template, context)
        text_content = strip_tags(html_content)

        email = EmailMultiAlternatives(subject, text_content, sender_email, [receiver_email])
        email.attach_alternative(html_content, "text/html")
        email.send()

        return Response({'detail': 'Se ha restablecido la contraseña. Se ha enviado un correo electrónico con la nueva contraseña.'}, status=status.HTTP_200_OK)
