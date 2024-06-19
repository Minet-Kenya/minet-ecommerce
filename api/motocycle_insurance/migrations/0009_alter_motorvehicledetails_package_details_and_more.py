# Generated by Django 5.0.4 on 2024-05-28 07:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motocycle_insurance', '0008_motorvehicledetails_vehicle_use'),
        ('users', '0003_alter_user_options_user_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motorvehicledetails',
            name='package_details',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
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
            bases=('motocycle_insurance.basemodel',),
        ),
    ]