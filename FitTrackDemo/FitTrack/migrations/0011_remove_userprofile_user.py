# Generated by Django 5.0.1 on 2024-02-05 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FitTrack', '0010_userprofile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
    ]
