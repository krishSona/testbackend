# Generated by Django 3.0.5 on 2020-10-29 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_auto_20201029_0835'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='employer',
            name='photo',
        ),
    ]
