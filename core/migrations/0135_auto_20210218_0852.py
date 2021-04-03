# Generated by Django 3.0.5 on 2021-02-18 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0134_application'),
    ]

    operations = [
        migrations.AddField(
            model_name='statement',
            name='fee',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='statement',
            name='gst',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='statement',
            name='withdraw',
            field=models.FloatField(blank=True, null=True),
        ),
    ]