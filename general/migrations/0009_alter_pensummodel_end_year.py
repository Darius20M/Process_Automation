# Generated by Django 4.2.5 on 2023-10-06 03:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0008_alter_pensummodel_start_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pensummodel',
            name='end_year',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
