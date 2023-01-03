from django.db import models
from django.db.models import Avg
from django.apps import apps

# Create your models here.
class Gestion(models.Model):
    gestion = models.PositiveBigIntegerField(
        blank=False,
        null=False,
        unique=True
    )
    activa = models.BooleanField(
        blank=False,
        null=False,
        default=True
    )
    def media_gestion(self):
        return apps.get_model('ppoa','Iniciativa').objects.filter(unidadgestion__gestion=self).values(
            'unidadgestion__unidad__nombre',
        ).annotate(
            media=Avg('unidadgestion__iniciativa__porcentaje'),
        ).aggregate(
            mediat=Avg('media'),
        )['mediat']
    def __str__(self):
        return str(self.gestion)

class Unidad(models.Model):
    nombre = models.CharField(
        max_length=300,
        blank=False,
        null=False
    )
    email_unidad = models.EmailField(
        max_length=254,
        blank=True,
        null=True
    )
    def __str__(self):
        return self.nombre
