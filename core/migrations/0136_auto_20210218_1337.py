# Generated by Django 3.0.5 on 2021-02-18 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0135_auto_20210218_0852'),
    ]

    operations = [
        migrations.RenameField(
            model_name='statement',
            old_name='fee',
            new_name='fees',
        ),
    ]
