# Generated by Django 3.0.5 on 2020-10-09 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20201009_1250'),
        ('authentication', '0004_auto_20201009_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='company_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.Company'),
        ),
    ]
