# Generated by Django 3.0.5 on 2021-01-27 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0112_auto_20210127_1059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='fcm_device',
        ),
    ]