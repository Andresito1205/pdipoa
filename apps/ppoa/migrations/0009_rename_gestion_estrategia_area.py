# Generated by Django 4.0.1 on 2022-01-23 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ppoa', '0008_estrategia_iniciativapdi_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estrategia',
            old_name='gestion',
            new_name='area',
        ),
    ]
