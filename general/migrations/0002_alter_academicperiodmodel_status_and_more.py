# Generated by Django 4.2.5 on 2023-09-27 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicperiodmodel',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('approved', 'Approved'), ('failed', 'Failed'), ('due', 'Due'), ('ongoing', 'Ongoing')], default='active', max_length=10),
        ),
        migrations.AlterField(
            model_name='careermodel',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('approved', 'Approved'), ('failed', 'Failed'), ('due', 'Due'), ('ongoing', 'Ongoing')], default='active', max_length=10),
        ),
        migrations.AlterField(
            model_name='classroommodel',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('approved', 'Approved'), ('failed', 'Failed'), ('due', 'Due'), ('ongoing', 'Ongoing')], default='active', max_length=10),
        ),
        migrations.AlterField(
            model_name='pensummodel',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('approved', 'Approved'), ('failed', 'Failed'), ('due', 'Due'), ('ongoing', 'Ongoing')], default='active', max_length=10),
        ),
        migrations.AlterField(
            model_name='pensumsubjectmodel',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('approved', 'Approved'), ('failed', 'Failed'), ('due', 'Due'), ('ongoing', 'Ongoing')], default='active', max_length=10),
        ),
    ]
