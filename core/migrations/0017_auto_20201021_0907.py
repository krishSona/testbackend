# Generated by Django 3.0.5 on 2020-10-21 09:07

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20201017_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='agreed_with_terms_and_conditions',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='salary_type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='weekly_holidays',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), blank=True, null=True, size=None),
        ),
    ]
