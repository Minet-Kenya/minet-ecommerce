# Generated by Django 5.0.4 on 2024-05-16 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motocycle_insurance', '0005_motorvehicledetails_payment_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='motorcyclecoverdetails',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Complete', 'Complete')], default='Pending', max_length=25),
        ),
        migrations.AddField(
            model_name='motorvehicledetails',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Complete', 'Complete')], default='Pending', max_length=25),
        ),
    ]
