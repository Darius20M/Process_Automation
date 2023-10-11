import random
from datetime import timedelta

from django.contrib.auth.models import User
from django.core.management import BaseCommand
from django.utils import timezone
from django.utils.timezone import localtime
from faker import Faker

from accounts.models import StudentProfileModel, RoleModel, DeanModel, DirectorModel
from general.models import FacultyModel, SchoolModel


class Command(BaseCommand):
    help = "Generate data dummy for sample"

    def is_user_already(self):
        fake = Faker()
        while True:
            current_year = timezone.now().year
            random_year = random.randint(2016, current_year)
            random_digits = ''.join([str(random.randint(0, 9)) for _ in range(4)])
            teacher_id = f"{random_year}-{random_digits}"


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
        faculty_names = ['Facultad Ciencias de la Salud', 'Facultad de Humanidades y Educación', 'Facultad Ciencias Económicas y Administrativas',
                         'Facultad Ciencias Jurídicas y Políticas', 'Facultad Ciencias Sociales y de La Comunicación', 'Facultad Arquitectura Y Bellas Artes',
                         'Facultad Ciencias Religiosas.','Facultad Ciencia y Tecnología.']

        for i in faculty_names:

            user = User.objects.create_user(
                username=self.is_user_already(),
                email=fake.unique.email(),
                password='Test12345',
                first_name=fake.unique.first_name(),
                last_name=fake.unique.last_name()
            )

            role = RoleModel.objects.get(code='dean_rol')

            dean = DeanModel.objects.create(
                    user=user,
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    dean_id=user.username,
                    date_of_birth=fake.date_of_birth(),
                    role=role,
                    gender=fake.random_element(elements=('Male', 'Female', 'Other')),
                    address=fake.address()[0:255],
                    contact_phone=fake.phone_number()[0:14],
                    email=fake.unique.email(),
                    enrollment_status = 'Enrolled',
                    identification_number=fake.unique.random_number(digits=10),

            )



            faculty = FacultyModel(
                name=i,
                dean=dean,
                description=fake.paragraph(),
                established_date=fake.date_of_birth(minimum_age=20, maximum_age=70),
                website=fake.url(),
                contact_email=fake.email(),
                phone_number=fake.phone_number()[0:14],

            )
            faculty.save()

            user = User.objects.create_user(
                username=self.is_user_already(),
                email=fake.unique.email(),
                password='Test12345',
                first_name=fake.unique.first_name(),
                last_name=fake.unique.last_name()
            )

            role = RoleModel.objects.get(code='director_rol')

            director = DirectorModel(
                user=user,
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                director_id=user.username,
                date_of_birth=fake.date_of_birth(),
                role=role,
                gender=fake.random_element(elements=('Male', 'Female', 'Other')),
                address=fake.address()[0:255],
                contact_phone=fake.phone_number()[0:14],
                email=fake.unique.email(),
                enrollment_status='Inactive',
                identification_number=fake.unique.random_number(digits=10),

            )
            director.save()

            school = SchoolModel(
                name=fake.company(),
                director=director,
                faculty=faculty,
                description=fake.paragraph(),
                established_date=fake.date_of_birth(minimum_age=20, maximum_age=70),
                website=fake.url(),
                contact_email=fake.email(),
                phone_number=fake.phone_number()[0:14],

            )

            school.save()



