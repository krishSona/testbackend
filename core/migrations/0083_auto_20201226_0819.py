# Generated by Django 3.0.5 on 2020-12-26 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0082_auto_20201226_0602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='gstin',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
