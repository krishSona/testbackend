# Generated by Django 3.0.5 on 2020-11-17 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0057_auto_20201116_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='beneficiary_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
