# Generated by Django 3.0.5 on 2021-02-05 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0118_attendance_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]