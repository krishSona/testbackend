# Generated by Django 3.0.5 on 2021-03-26 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0144_auto_20210326_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(db_index=True),
        ),
    ]
