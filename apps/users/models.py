from django.db import models

# Create your models here.
class Permisos(models.Model):
    class Meta:
        permissions = (
            ('users','Permiso al modulo de usuarios'),
            ('gestion','Permiso al Modulo de gestion'),
            ('ppoa','Permiso al Modeulo de Planificaion del POA'),
            ('evaluacion', 'Permiso al Modulo de Evaluacion')
        )
