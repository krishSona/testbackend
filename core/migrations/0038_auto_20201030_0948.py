# Generated by Django 3.0.5 on 2020-10-30 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0037_auto_20201030_0938'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='duration',
            field=models.CharField(blank=True, db_index=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='end_at',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='face_detected',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='qr_code_scanned',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='start_at',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='status',
            field=models.CharField(db_index=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='work_location',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(db_index=True),
        ),
    ]
