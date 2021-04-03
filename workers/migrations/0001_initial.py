# Generated by Django 3.0.5 on 2020-04-30 04:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=18)),
            ],
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('salary_month', models.CharField(max_length=50)),
                ('payment_date', models.DateField(null=True)),
                ('no_of_workers', models.IntegerField()),
                ('total_salary_amount', models.IntegerField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('aadhaar_number', models.CharField(max_length=12)),
                ('total_salary', models.IntegerField(default=0)),
                ('advance_taken', models.IntegerField(default=0)),
                ('status', models.BooleanField(null=True)),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='workers.Account')),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='workers.City')),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='workers.Company')),
                ('designation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='workers.Designation')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_salary', models.IntegerField()),
                ('advance_taken', models.IntegerField()),
                ('net_salary', models.IntegerField()),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='workers.Payment')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='workers.Worker')),
            ],
        ),
        migrations.CreateModel(
            name='Ifscode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=11)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='workers.Bank')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='ifscode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='workers.Ifscode'),
        ),
    ]
