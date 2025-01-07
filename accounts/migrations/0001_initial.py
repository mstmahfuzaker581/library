# Generated by Django 5.1.4 on 2025-01-07 08:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField(default=0)),
                ('address', models.CharField(max_length=2049)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_account', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]