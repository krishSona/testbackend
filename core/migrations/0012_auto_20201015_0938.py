# Generated by Django 3.0.5 on 2020-10-15 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20201014_0422'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='address_proof_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='id_proof_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
