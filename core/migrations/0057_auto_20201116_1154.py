# Generated by Django 3.0.5 on 2020-11-16 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0056_auto_20201116_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='work_timings',
            field=models.CharField(default='9:00 AM-6:00 PM', max_length=17, null=True),
        ),
    ]
