# Generated by Django 3.0.5 on 2020-11-20 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0068_auto_20201120_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='work_timings',
            field=models.CharField(default='9:00 AM-6:00 PM', max_length=17),
        ),
    ]
