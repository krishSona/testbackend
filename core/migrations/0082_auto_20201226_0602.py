# Generated by Django 3.0.5 on 2020-12-26 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0081_auto_20201224_0543'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='qrcode',
            constraint=models.UniqueConstraint(fields=('qr_id', 'longitude', 'latitude'), name='unique_qr_id_longitude_latitude'),
        ),
    ]
