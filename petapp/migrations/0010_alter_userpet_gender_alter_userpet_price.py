# Generated by Django 5.0.1 on 2024-12-08 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petapp', '0009_vaccinations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpet',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=50),
        ),
        migrations.AlterField(
            model_name='userpet',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
