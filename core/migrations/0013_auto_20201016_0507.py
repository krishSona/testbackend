# Generated by Django 3.0.5 on 2020-10-16 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20201015_0938'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='aadhaar_number',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='pan',
        ),
    ]
