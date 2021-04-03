# Generated by Django 3.0.5 on 2021-01-25 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0105_company_tie_up'),
    ]

    operations = [
        migrations.RenameField(
            model_name='statement',
            old_name='closing_balance',
            new_name='balance',
        ),
        migrations.RenameField(
            model_name='statement',
            old_name='opening_balance',
            new_name='current_due',
        ),
        migrations.AddField(
            model_name='statement',
            name='interest',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='statement',
            name='previous_due',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
