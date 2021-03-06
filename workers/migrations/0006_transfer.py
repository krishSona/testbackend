# Generated by Django 3.0.5 on 2020-05-09 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0005_account_beneficiary_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('utr', models.CharField(max_length=30, null=True)),
                ('status', models.CharField(max_length=20, null=True)),
                ('detail', models.CharField(max_length=150, null=True)),
                ('processed_on', models.DateTimeField(null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='workers.Account')),
            ],
        ),
    ]
