# Generated by Django 3.0.5 on 2021-02-17 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0133_auto_20210216_1439'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('company_email', models.CharField(blank=True, max_length=255, null=True)),
                ('employee_id', models.CharField(blank=True, max_length=255, null=True)),
                ('company_name', models.CharField(blank=True, max_length=255, null=True)),
                ('net_monthly_salary', models.CharField(blank=True, max_length=255, null=True)),
                ('salary_day', models.CharField(blank=True, max_length=255, null=True)),
                ('bank_name', models.CharField(blank=True, max_length=255, null=True)),
                ('bank_account_name', models.CharField(blank=True, max_length=255, null=True)),
                ('bank_account_number1', models.CharField(blank=True, max_length=255, null=True)),
                ('bank_account_number2', models.CharField(blank=True, max_length=255, null=True)),
                ('ifsc', models.CharField(blank=True, max_length=255, null=True)),
                ('utm_source', models.CharField(blank=True, max_length=255, null=True)),
                ('utm_medium', models.CharField(blank=True, max_length=255, null=True)),
                ('utm_campaign', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
