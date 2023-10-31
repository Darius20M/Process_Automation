# Generated by Django 4.0 on 2023-10-30 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_studentprofilemodel_user'),
        ('general', '0009_rename_max_student_become_special_universityrulemodel_min_student_become_special'),
        ('catalog', '0005_classmodel_student_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjectstudentmodel',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='subject_student', to='accounts.studentprofilemodel'),
        ),
        migrations.AlterField(
            model_name='subjectstudentmodel',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='subject_student', to='general.subjectmodel'),
        ),
    ]