# Generated by Django 3.0.5 on 2021-02-10 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0121_verifier_counter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]
