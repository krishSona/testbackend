# Generated by Django 3.0.5 on 2020-10-17 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20201017_0537'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='coi_image',
        ),
        migrations.RemoveField(
            model_name='company',
            name='pan_image',
        ),
    ]
