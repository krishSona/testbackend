# Generated by Django 3.0.5 on 2021-01-25 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0108_remove_statement_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='due_date',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='salary_date',
        ),
        migrations.AddField(
            model_name='employee',
            name='due_day',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='salary_day',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
