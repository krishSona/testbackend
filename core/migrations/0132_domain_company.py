# Generated by Django 3.0.5 on 2021-02-16 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0131_auto_20210216_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='domain',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.Company'),
        ),
    ]
