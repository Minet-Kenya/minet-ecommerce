# Generated by Django 5.0.4 on 2024-05-16 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance_packages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='category',
            field=models.CharField(choices=[('Motorcycle', 'Motorcycle'), ('Motor', 'Motor')], default='default', max_length=25),
        ),
    ]
