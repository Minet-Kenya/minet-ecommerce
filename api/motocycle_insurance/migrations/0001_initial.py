# Generated by Django 5.0.4 on 2024-06-29 06:53

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
        ('insurance_packages', '0001_initial'),
        ('users', '0002_alter_user_idnumber_alter_user_krapin'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('last_modified', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='EducationPolicy',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='motocycle_insurance.basemodel')),
                ('full_names', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('plan_type', models.CharField(max_length=100)),
                ('addational_info', models.CharField(max_length=500)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.client')),
            ],
            options={
                'ordering': ['-created_at'],
            },
            bases=('motocycle_insurance.basemodel',),
        ),
        migrations.CreateModel(
            name='MotorCycleCoverDetails',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='motocycle_insurance.basemodel')),
                ('registration_no', models.CharField(max_length=100, unique=True)),
                ('log_book_no', models.CharField(max_length=100, unique=True)),
                ('make', models.CharField(max_length=100)),
                ('manufacture_year', models.DateField()),
                ('engine_cc', models.CharField(max_length=100)),
                ('policy_details', models.JSONField(blank=True, null=True)),
                ('motorcycle_and_rider_details', models.JSONField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Complete', 'Complete')], default='Pending', max_length=25)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.client')),
                ('package_details', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='insurance_packages.package')),
                ('payment_details', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.transactions')),
            ],
            options={
                'ordering': ['-created_at'],
            },
            bases=('motocycle_insurance.basemodel',),
        ),
        migrations.CreateModel(
            name='MotorVehicleDetails',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='motocycle_insurance.basemodel')),
                ('registration_no', models.CharField(max_length=100, unique=True)),
                ('make', models.CharField(max_length=100)),
                ('manufacture_year', models.CharField(max_length=100)),
                ('policy_type', models.CharField(max_length=100)),
                ('policy_period', models.DateField()),
                ('car_value', models.CharField(max_length=100)),
                ('engine_cc', models.CharField(max_length=100)),
                ('engine_no', models.CharField(max_length=100)),
                ('vehicle_use', models.CharField(max_length=100)),
                ('package_details', models.CharField(max_length=100)),
                ('policy_details', models.JSONField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Complete', 'Complete')], default='Pending', max_length=25)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.client')),
                ('payment_details', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.transactions')),
            ],
            options={
                'ordering': ['-created_at'],
            },
            bases=('motocycle_insurance.basemodel',),
        ),
        migrations.CreateModel(
            name='OtherPolicies',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='motocycle_insurance.basemodel')),
                ('policy_details', models.JSONField(blank=True, null=True)),
                ('policy_type', models.CharField(choices=[('Education Policy', 'Education Policy'), ('Home Insurance', 'Home Insurance'), ('Medical Insurance', 'Medical Insurance'), ('Individual Life', 'Individual Life'), ('Travel Insurance', 'Travel Insurance'), ('Golfers Insurance', 'Golfers Insurance'), ('Personal Accident', 'Personal Accident')], default='', max_length=25)),
                ('infomation_details', models.JSONField(blank=True, null=True)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.client')),
            ],
            options={
                'ordering': ['created_at'],
            },
            bases=('motocycle_insurance.basemodel',),
        ),
    ]