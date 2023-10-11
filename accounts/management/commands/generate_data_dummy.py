import random
from datetime import timedelta

from django.contrib.auth.models import User
from django.core.management import BaseCommand
from django.utils import timezone
from django.utils.timezone import localtime
from faker import Faker

from accounts.models import StudentProfileModel, RoleModel


class Command(BaseCommand):
    help = "Generate data dummy for sample"

    def is_user_already(self):
        fake = Faker()
        while True:
            current_year = timezone.now().year
            random_digits = ''.join([str(random.randint(0, 9)) for _ in range(4)])
            teacher_id = f"{current_year}-{random_digits}"


            if not User.objects.filter(username=teacher_id).exists():
                self.stdout.write(
                    self.style.NOTICE('Verifying user..."')
                )
                return teacher_id

            self.stdout.write(
                self.style.NOTICE(' user already exist..."')
            )

    def __init__(self, stdout=None, stderr=None, no_color=False, force_color=False):
        super().__init__(stdout, stderr, no_color, force_color)

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.NOTICE('Initialize data dummy..."')
        )
        fake = Faker()

        for i in range(1, 10):

            user = User.objects.create_user(
                username=self.is_user_already(),
                email=fake.unique.email(),
                password='Test12345',
                first_name=fake.unique.first_name(),
                last_name=fake.unique.last_name()
            )

            for i in range(1,100):

                user = User.objects.create_user(
                    username=self.is_user_already(),
                    email=fake.unique.email(),
                    password='Test12345',
                    first_name=fake.unique.first_name(),
                    last_name=fake.unique.last_name()
                    )

                role = RoleModel.objects.get(code='student_rol')  # Reemplaza 'NombreDelRol' con el nombre del rol

                student_profile = StudentProfileModel.objects.create(
                    user=user,
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    student_id=user.username,
                    #career
                    date_of_birth=fake.date_of_birth(),
                    role=role,
                    gender=fake.random_element(elements=('Male', 'Female', 'Other')),
                    address=fake.address()[0:255],
                    contact_phone=fake.phone_number()[0:14],
                    email=fake.unique.email(),
                    identification_number=fake.unique.random_number(digits=10),

                )

