# Generated by Django 3.0.5 on 2020-10-27 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_auto_20201024_1018'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='weekly_working_days',
            new_name='work_days',
        ),
        migrations.AddField(
            model_name='employee',
            name='work_timings',
            field=models.CharField(default='9AM-6PM', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='salary_type',
            field=models.CharField(blank=True, default='net', max_length=50, null=True),
        ),
    ]
