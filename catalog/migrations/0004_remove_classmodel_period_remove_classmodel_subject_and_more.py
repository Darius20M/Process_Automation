# Generated by Django 4.2.5 on 2023-10-03 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_careerstudentmodel_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classmodel',
            name='period',
        ),
        migrations.RemoveField(
            model_name='classmodel',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='classmodel',
            name='teacher',
        ),
        migrations.RemoveField(
            model_name='scheduleclassmodel',
            name='_class',
        ),
        migrations.RemoveField(
            model_name='scheduleclassmodel',
            name='classroom',
        ),
        migrations.RemoveField(
            model_name='scheduleclassmodel',
            name='teacher',
        ),
        migrations.RemoveField(
            model_name='schedulestudentmodel',
            name='_class',
        ),
        migrations.RemoveField(
            model_name='schedulestudentmodel',
            name='classroom',
        ),
        migrations.RemoveField(
            model_name='schedulestudentmodel',
            name='teacher',
        ),
        migrations.RemoveField(
            model_name='subjectstudentmodel',
            name='student',
        ),
        migrations.RemoveField(
            model_name='subjectstudentmodel',
            name='subject',
        ),
        migrations.DeleteModel(
            name='CareerStudentModel',
        ),
        migrations.DeleteModel(
            name='ClassModel',
        ),
        migrations.DeleteModel(
            name='ScheduleClassModel',
        ),
        migrations.DeleteModel(
            name='ScheduleStudentModel',
        ),
        migrations.DeleteModel(
            name='SubjectStudentModel',
        ),
    ]