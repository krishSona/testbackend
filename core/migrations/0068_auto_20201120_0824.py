# Generated by Django 3.0.5 on 2020-11-20 08:24

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0067_auto_20201120_0823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='work_days',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'days': ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']}),
        ),
    ]
