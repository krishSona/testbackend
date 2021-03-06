# Generated by Django 3.0.5 on 2021-01-27 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fcm_django', '0005_auto_20170808_1145'),
        ('core', '0111_auto_20210126_0608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='fcm_registration_token',
        ),
        migrations.AddField(
            model_name='employee',
            name='fcm_device',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='fcm_django.FCMDevice'),
        ),
    ]
