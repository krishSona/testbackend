# Generated by Django 3.0.5 on 2020-10-16 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20201016_0507'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kyc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('type', models.IntegerField(blank=True, null=True)),
                ('number', models.CharField(max_length=20, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='employee/kyc/')),
                ('verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='employee',
            name='address_proof_image',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='address_proof_number',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='id_proof_image',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='id_proof_number',
        ),
        migrations.AddField(
            model_name='employee',
            name='current_city',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='current_pincode',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='current_state',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='permanent_city',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='permanent_pincode',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='permanent_state',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='address_proof',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='employee_address_proof', to='core.Kyc'),
        ),
        migrations.AddField(
            model_name='employee',
            name='id_proof',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='employee_id_proof', to='core.Kyc'),
        ),
    ]