# Generated by Django 4.0 on 2023-10-30 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_studentprofilemodel_user'),
        ('catalog', '0004_alter_classmodel_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='classmodel',
            name='student',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='accounts.studentprofilemodel'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='schedulestudentmodel',
            name='schedule',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='catalog.scheduleclassmodel'),
        ),
    ]
