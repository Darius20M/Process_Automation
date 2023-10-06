# Generated by Django 4.2.5 on 2023-10-05 23:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_studentprofilemodel_career'),
        ('general', '0004_alter_pensumsubjectmodel_prerequisites'),
        ('catalog', '0005_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secc', models.CharField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('approved', 'Approved'), ('failed', 'Failed'), ('due', 'Due'), ('ongoing', 'Ongoing')], default='active', max_length=10)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('period', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='general.academicperiodmodel')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='general.subjectmodel')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.teachermodel')),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleClassModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField()),
                ('h_start', models.DateTimeField()),
                ('h_end', models.DateTimeField()),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('approved', 'Approved'), ('failed', 'Failed'), ('due', 'Due'), ('ongoing', 'Ongoing')], default='active', max_length=10)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('_class', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.classmodel')),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='general.classroommodel')),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleStudentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('approved', 'Approved'), ('failed', 'Failed'), ('due', 'Due'), ('ongoing', 'Ongoing')], default='active', max_length=10)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.scheduleclassmodel')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.studentprofilemodel')),
            ],
        ),
        migrations.CreateModel(
            name='CareerStudentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('approved', 'Approved'), ('failed', 'Failed'), ('due', 'Due'), ('ongoing', 'Ongoing')], default='active', max_length=10)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='general.careermodel')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.studentprofilemodel')),
            ],
        ),
    ]
