# Generated by Django 4.2.5 on 2023-10-10 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_alter_deanmodel_dean_id'),
        ('general', '0012_alter_facultymodel_dean'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolmodel',
            name='director',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='schools', to='accounts.directormodel'),
        ),
        migrations.AlterField(
            model_name='schoolmodel',
            name='faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='schools', to='general.facultymodel'),
        ),
    ]
