# Generated by Django 4.0 on 2023-10-11 03:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeanModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('dean_id', models.CharField(max_length=10, unique=True)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('address', models.TextField()),
                ('contact_phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('identification_number', models.CharField(max_length=20, unique=True)),
                ('enrollment_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('enrollment_status', models.CharField(choices=[('Enrolled', 'Enrolled'), ('Inactive', 'Inactive')], max_length=20)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
            options={
                'verbose_name': 'Dean',
                'verbose_name_plural': 'Deans',
            },
        ),
        migrations.CreateModel(
            name='DirectorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('director_id', models.CharField(max_length=10, unique=True)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('address', models.TextField()),
                ('contact_phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('identification_number', models.CharField(max_length=20, unique=True)),
                ('enrollment_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('enrollment_status', models.CharField(choices=[('Enrolled', 'Enrolled'), ('Inactive', 'Inactive')], max_length=20)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
            options={
                'verbose_name': 'Director',
                'verbose_name_plural': 'Directors',
            },
        ),
        migrations.CreateModel(
            name='RoleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=180)),
                ('code', models.CharField(max_length=30, unique=True)),
                ('is_enabled', models.BooleanField(default=True)),
                ('about', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
            options={
                'verbose_name': 'Role',
                'verbose_name_plural': 'Roles',
            },
        ),
        migrations.CreateModel(
            name='StudentProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('student_id', models.CharField(max_length=9, unique=True)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('address', models.TextField()),
                ('contact_phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('identification_number', models.CharField(max_length=20, unique=True)),
                ('enrollment_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('enrollment_status', models.CharField(choices=[('Enrolled', 'Enrolled'), ('Graduated', 'Graduated')], default='N/A', max_length=20)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Students',
            },
        ),
        migrations.CreateModel(
            name='TeacherModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('teacher_id', models.CharField(max_length=8, unique=True)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('address', models.TextField()),
                ('contact_phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('identification_number', models.CharField(max_length=20, unique=True)),
                ('enrollment_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('enrollment_status', models.CharField(choices=[('Enrolled', 'Enrolled'), ('Graduated', 'Graduated')], max_length=20)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.rolemodel')),
            ],
            options={
                'verbose_name': 'Teacher',
                'verbose_name_plural': 'Teachers',
            },
        ),
    ]
