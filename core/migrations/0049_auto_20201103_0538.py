# Generated by Django 3.0.5 on 2020-11-03 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0048_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='designation',
            field=models.CharField(max_length=255, null=True),
        ),
    ]