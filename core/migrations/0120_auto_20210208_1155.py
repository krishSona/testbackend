# Generated by Django 3.0.5 on 2021-02-08 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0119_attendance_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='verifier',
            name='employee',
        ),
        migrations.AddField(
            model_name='verifier',
            name='employee',
            field=models.ManyToManyField(to='core.Employee'),
        ),
    ]
