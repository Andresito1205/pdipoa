# Generated by Django 4.0.1 on 2022-01-15 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0004_alter_gestion_gestion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unidad',
            name='gestion',
        ),
    ]