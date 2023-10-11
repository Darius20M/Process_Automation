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


    def __init__(self, stdout=None, stderr=None, no_color=False, force_color=False):
        super().__init__(stdout, stderr, no_color, force_color)

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.NOTICE('Initialize data dummy..."')
        )
        fake = Faker()

        academic_periods = [
            {
                "name": "Periodo Academico Septiembre-Deciembre 2023",
                "start_date": "2023-09-01",
                "end_date": "2023-12-11",
                "description": "Periodo Academico Septiembre-Deciembre 2023.",
                "status": "Active"
            },
            {
                "name": "Periodo Academico Mayo-Agosto 2023",
                "start_date": "2023-05-01",
                "end_date": "2023-08-11",
                "description": "Periodo Academico Mayo-Agosto 2023",
                "status": "Inactive"
            }

        ]



