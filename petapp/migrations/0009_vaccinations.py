# Generated by Django 5.0.1 on 2024-12-08 03:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petapp', '0008_alter_pet_image_userpet_delete_vaccinations'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vaccinations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaccine_name', models.CharField(max_length=100)),
                ('batch_number', models.CharField(max_length=100)),
                ('veterinarian', models.CharField(max_length=100)),
                ('date_administered', models.DateTimeField(auto_now_add=True)),
                ('next_due_date', models.DateTimeField(auto_now_add=True)),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vaccinations', to='petapp.userpet')),
            ],
        ),
    ]
