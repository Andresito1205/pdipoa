# Generated by Django 4.0.1 on 2022-01-13 01:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_permisos_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='permisos',
            options={'permissions': (('users', 'Permiso al modulo de usuarios'), ('gestion', 'Permiso al Modulo de gestion'), ('ppoa', 'Permiso al Modeulo de Planificaion del POA'))},
        ),
    ]
