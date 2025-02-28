# Generated by Django 5.0.1 on 2024-12-08 05:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petapp', '0011_remove_userpet_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='PetInsurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider', models.CharField(max_length=255)),
                ('policy_number', models.CharField(max_length=255)),
                ('coverage', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pet', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='insurance', to='petapp.userpet')),
            ],
        ),
    ]
