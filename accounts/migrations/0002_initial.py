# Generated by Django 4.0 on 2023-10-11 03:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('general', '0001_initial'),
        ('accounts', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachermodel',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='general.schoolmodel'),
        ),
        migrations.AddField(
            model_name='teachermodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
        migrations.AddField(
            model_name='studentprofilemodel',
            name='career',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='general.careermodel'),
        ),
        migrations.AddField(
            model_name='studentprofilemodel',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.rolemodel'),
        ),
        migrations.AddField(
            model_name='studentprofilemodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
        migrations.AddField(
            model_name='directormodel',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.rolemodel'),
        ),
        migrations.AddField(
            model_name='directormodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
        migrations.AddField(
            model_name='deanmodel',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.rolemodel'),
        ),
        migrations.AddField(
            model_name='deanmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
