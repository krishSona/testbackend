# Generated by Django 3.0.5 on 2020-11-09 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0049_auto_20201103_0538'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]