# Generated by Django 4.2.6 on 2023-10-20 22:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import localflavor.us.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_1', models.CharField(blank=True, max_length=128)),
                ('address_2', models.CharField(blank=True, max_length=128)),
                ('city', models.CharField(max_length=64)),
                ('state', localflavor.us.models.USStateField(default='NY', max_length=2)),
                ('zip_code', localflavor.us.models.USZipCodeField(blank=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(blank=True, max_length=140)),
                ('phone_number', models.CharField(blank=True, max_length=12)),
                ('location', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.location')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]