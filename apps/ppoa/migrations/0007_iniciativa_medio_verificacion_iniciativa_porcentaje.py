# Generated by Django 4.0.1 on 2022-01-20 21:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ppoa', '0006_unidadgestion_foda'),
    ]

    operations = [
        migrations.AddField(
            model_name='iniciativa',
            name='medio_verificacion',
            field=models.TextField(blank=True, null=True, verbose_name='Medio de Verificacion'),
        ),
        migrations.AddField(
            model_name='iniciativa',
            name='porcentaje',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.RegexValidator(code='0001', message='Solo se permiten numeros del 0 al 100', regex='^([0-9]|[1-9][0-9]|[100]){5}$')]),
        ),
    ]
