# Generated by Django 3.0.5 on 2021-01-22 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0104_employee_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='tie_up',
            field=models.BooleanField(default=False),
        ),
    ]
