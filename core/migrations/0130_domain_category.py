# Generated by Django 3.0.5 on 2021-02-16 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0129_auto_20210213_0951'),
    ]

    operations = [
        migrations.AddField(
            model_name='domain',
            name='category',
            field=models.IntegerField(blank=True, choices=[(0, 'generic'), (1, 'company')], null=True),
        ),
    ]