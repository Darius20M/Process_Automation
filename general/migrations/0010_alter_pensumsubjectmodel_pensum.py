# Generated by Django 4.0 on 2023-10-30 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0009_rename_max_student_become_special_universityrulemodel_min_student_become_special'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pensumsubjectmodel',
            name='pensum',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pensums', to='general.pensummodel'),
        ),
    ]