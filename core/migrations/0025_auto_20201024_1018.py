# Generated by Django 3.0.5 on 2020-10-24 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_employee_weekly_working_days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='service_status',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
