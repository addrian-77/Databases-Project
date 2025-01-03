# Generated by Django 5.1.4 on 2025-01-03 20:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('technologies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaintenanceRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('technology', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='technologies.technology')),
            ],
        ),
    ]
