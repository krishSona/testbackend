# Generated by Django 3.0.5 on 2020-10-30 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_auto_20201030_0705'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='location',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='present',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='start_time',
        ),
    ]
