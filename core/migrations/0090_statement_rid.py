# Generated by Django 3.0.5 on 2021-01-06 08:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0089_auto_20201230_0809'),
    ]

    operations = [
        migrations.AddField(
            model_name='statement',
            name='rid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
