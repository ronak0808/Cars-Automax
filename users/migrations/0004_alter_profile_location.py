# Generated by Django 5.0.3 on 2024-03-29 20:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_location_state_profile_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.location'),
        ),
    ]
