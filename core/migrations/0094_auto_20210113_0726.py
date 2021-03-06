# Generated by Django 3.0.5 on 2021-01-13 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0093_company_domain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.City'),
        ),
        migrations.AlterField(
            model_name='company',
            name='employee_range',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.EmployeeRange'),
        ),
        migrations.AlterField(
            model_name='company',
            name='gstin',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='industry',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.Industry'),
        ),
        migrations.AlterField(
            model_name='company',
            name='office_address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='pincode',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.State'),
        ),
    ]
