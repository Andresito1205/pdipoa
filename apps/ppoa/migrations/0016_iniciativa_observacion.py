# Generated by Django 4.0.6 on 2022-09-18 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ppoa', '0015_iniciativa_presupuesto'),
    ]

    operations = [
        migrations.AddField(
            model_name='iniciativa',
            name='observacion',
            field=models.TextField(blank=True, null=True, verbose_name='obervaciones'),
        ),
    ]
