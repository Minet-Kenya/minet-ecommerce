# Generated by Django 5.0.4 on 2024-05-12 12:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motocycle_insurance', '0002_motorcyclecoverdetails_package_details_and_more'),
        ('users', '0003_alter_user_options_user_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MotorVehicleDetails',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='motocycle_insurance.basemodel')),
                ('registration_no', models.CharField(max_length=100, unique=True)),
                ('make', models.CharField(max_length=100)),
                ('manufacture_year', models.DateField()),
                ('policy_type', models.CharField(max_length=100)),
                ('policy_period', models.DateField()),
                ('car_value', models.CharField(max_length=100)),
                ('engine_cc', models.CharField(max_length=100)),
                ('engine_no', models.CharField(max_length=100)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.client')),
            ],
            options={
                'ordering': ['-created_at'],
            },
            bases=('motocycle_insurance.basemodel',),
        ),
    ]