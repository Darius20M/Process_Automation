# Generated by Django 4.2.5 on 2023-10-10 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_deanmodel_enrollment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='directormodel',
            name='enrollment_status',
            field=models.CharField(choices=[('Enrolled', 'Enrolled'), ('Inactive', 'Inactive')], max_length=20),
        ),
    ]