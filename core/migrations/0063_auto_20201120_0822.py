# Generated by Django 3.0.5 on 2020-11-20 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0062_auto_20201120_0820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='agreed_with_terms_and_conditions',
            field=models.BooleanField(default=False),
        ),
    ]
