# Generated by Django 4.0 on 2023-10-27 04:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0006_universityrulemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='academicperiodmodel',
            name='next_period',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='next_cademic', to='general.academicperiodmodel'),
        ),
    ]
