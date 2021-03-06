# Generated by Django 3.0.5 on 2020-10-10 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20201010_0923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='coi_url',
        ),
        migrations.RemoveField(
            model_name='company',
            name='pan_url',
        ),
        migrations.AddField(
            model_name='company',
            name='coi_image',
            field=models.ImageField(blank=True, null=True, upload_to='company/kyc/coi/'),
        ),
        migrations.AddField(
            model_name='company',
            name='pan_image',
            field=models.ImageField(blank=True, null=True, upload_to='company/kyc/pan/'),
        ),
        migrations.AddField(
            model_name='employee',
            name='address_proof_image',
            field=models.ImageField(blank=True, null=True, upload_to='employee/kyc/address_proof_image/'),
        ),
        migrations.AddField(
            model_name='employee',
            name='id_proof_image',
            field=models.ImageField(blank=True, null=True, upload_to='employee/kyc/id_proof_image/'),
        ),
    ]
