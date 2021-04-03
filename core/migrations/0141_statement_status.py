# Generated by Django 3.0.5 on 2021-03-15 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0140_application_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='statement',
            name='status',
            field=models.CharField(choices=[('initialized', 'initialized'), ('pending', 'pending'), ('waiting', 'waiting'), ('rejected', 'rejected'), ('approved', 'approved'), ('cancelled', 'cancelled'), ('completed', 'completed')], default='initialized', max_length=15),
        ),
    ]