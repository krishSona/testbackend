# Generated by Django 3.0.5 on 2020-10-30 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_attendance'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='last_attendance_on',
            field=models.DateField(blank=True, null=True),
        ),
    ]
