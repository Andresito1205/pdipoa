# Generated by Django 4.0.1 on 2022-01-16 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ppoa', '0005_alter_foda_codigo'),
    ]

    operations = [
        migrations.AddField(
            model_name='unidadgestion',
            name='foda',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ppoa.foda'),
            preserve_default=False,
        ),
    ]
