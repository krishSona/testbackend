# Generated by Django 3.0.5 on 2020-12-01 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0073_auto_20201201_0646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrcode',
            name='qr_id',
            field=models.CharField(max_length=23),
        ),
    ]
