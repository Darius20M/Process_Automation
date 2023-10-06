# Generated by Django 4.2.5 on 2023-10-06 02:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0005_subjectmodel_created_subjectmodel_modified'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='academicperiodmodel',
            options={'verbose_name': 'Academic Period', 'verbose_name_plural': 'Academic Periods'},
        ),
        migrations.AlterModelOptions(
            name='careermodel',
            options={'verbose_name': 'Career', 'verbose_name_plural': 'Careers'},
        ),
        migrations.AlterModelOptions(
            name='classroommodel',
            options={'verbose_name': 'Classroom', 'verbose_name_plural': 'Classrooms'},
        ),
        migrations.AlterModelOptions(
            name='facultymodel',
            options={'verbose_name': 'faculties', 'verbose_name_plural': 'faculties'},
        ),
        migrations.AlterModelOptions(
            name='pensummodel',
            options={'verbose_name': 'Pensum', 'verbose_name_plural': 'Pensums'},
        ),
        migrations.AlterModelOptions(
            name='pensumsubjectmodel',
            options={'verbose_name': 'Pensum detail', 'verbose_name_plural': 'Pensum details'},
        ),
        migrations.AlterModelOptions(
            name='schoolmodel',
            options={'verbose_name': 'School', 'verbose_name_plural': 'Schools'},
        ),
        migrations.AlterModelOptions(
            name='subjectmodel',
            options={'verbose_name': 'Subject', 'verbose_name_plural': 'Subjects '},
        ),
    ]
