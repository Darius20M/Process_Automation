# Generated by Django 4.0 on 2023-10-11 03:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(default='Information', max_length=30)),
                ('title', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('unread', models.BooleanField(default=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='auth.user')),
            ],
            options={
                'db_table': 'sec_notifications_t',
            },
        ),
        migrations.CreateModel(
            name='ActivityModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_text', models.TextField()),
                ('level', models.CharField(default='Information', max_length=30)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='activities', to='auth.user')),
            ],
            options={
                'db_table': 'sec_activities_t',
            },
        ),
    ]
