# Generated by Django 4.2.5 on 2024-06-03 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motocycle_insurance', '0010_motorvehicledetails_policy_details_otherpolicies'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='educationpolicy',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='otherpolicies',
            options={'ordering': ['-created_at']},
        ),
        migrations.RenameField(
            model_name='otherpolicies',
            old_name='policy_detatils',
            new_name='infomation_details',
        ),
        migrations.AddField(
            model_name='otherpolicies',
            name='policy_details',
            field=models.JSONField(blank=True, null=True),
        ),
    ]