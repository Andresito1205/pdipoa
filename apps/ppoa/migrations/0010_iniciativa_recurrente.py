# Generated by Django 4.0.1 on 2022-01-23 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ppoa', '0009_rename_gestion_estrategia_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='iniciativa',
            name='recurrente',
            field=models.BooleanField(default=False),
        ),
    ]
