import random
from django.contrib.auth.models import User
from django.utils import timezone
from faker import Faker
def is_user_already():
    while True:
        current_year = timezone.now().year
        random_year = random.randint(2016, current_year)
        random_digits = ''.join([str(random.randint(0, 9)) for _ in range(4)])
        student = f"{random_year}-{random_digits}"

        if not User.objects.filter(username=student).exists():
            return student

