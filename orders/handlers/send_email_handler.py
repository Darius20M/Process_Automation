from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_email_handler(instance, email_type):
    sender_email = 'UCSD <dariusjosedelacruzhilario@gmail.com>'
    receiver_email = instance.user.email

    if email_type == 'confirmation':
        subject = 'Confirmación de solicitud de tutoría'
        email_template = 'request_email.html'
        # Contenido específico para la confirmación
    elif email_type == 'approval':
        subject = 'Notificación de aprobación'
        email_template = 'approval_email.html'

    elif email_type == 'deny':
        subject = 'Notificación de negacion'
        email_template = 'deny_email.html'
        # Contenido específico para la notificación de aprobación
    elif email_type == 'user_creation':
        subject = 'Bienvenido a nuestra plataforma'
        email_template = 'user_creation_email.html'
        # Contenido específico para el correo de creación de usuario

    context = {
        'inf': instance,
        # Otros datos específicos para el tipo de correo de creación de usuario
    }

    html_content = render_to_string(email_template, context)
    text_content = strip_tags(html_content)

    email = EmailMultiAlternatives(subject, text_content, sender_email, [receiver_email])
    email.attach_alternative(html_content, "text/html")
    email.send()

