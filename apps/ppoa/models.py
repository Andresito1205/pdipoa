from django.db import models
from django.db.models.deletion import CASCADE
from django.core.validators import RegexValidator
from smart_selects.db_fields import ChainedForeignKey
from django.db.models import Avg

# Create your models here.

class Area(models.Model):
    gestion = models.ForeignKey('gestion.Gestion', on_delete=models.CASCADE)
    nombre = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    def __str__(self):
        return self.nombre

class Estrategia(models.Model):
    area = models.ForeignKey('ppoa.Area', on_delete=models.CASCADE)
    codigo_foda = models.CharField(
        verbose_name='Codigo de Foda',
        max_length=10,
        null=False,
        blank=False,
        choices=(
            ('DA','DA'),
            ('FO','FO'),
            ('DO','DO'),
            ('FA','FA')
        )
    )
    estrategia = models.CharField(
        max_length=300,
        null=False,
        blank=False
    )
    descripcion = models.TextField(
        null=False,
        blank=False
    )
    def __str__(self):
        return self.codigo_foda + " " + self.estrategia

class ObjetivoEstrategico(models.Model):
    estrategia = models.ForeignKey('ppoa.Estrategia', on_delete=models.CASCADE)
    objetivo = models.TextField(
        null=False,
        blank=False
    )
    def __str__(self):
        return self.objetivo

class Perspectiva(models.Model):
    objetivoestrategico = models.ForeignKey('ppoa.ObjetivoEstrategico', on_delete=models.CASCADE)
    codigo = models.CharField(
        max_length=400,
        null=False,
        blank=False
    )
    perspectiva = models.CharField(
        max_length=400,
        null=False,
        blank=False
    )
    objetivo = models.TextField(
        null=False,
        blank=False
    )
    def __str__(self):
        return self.perspectiva

class IniciativaPDI(models.Model):
    perspectiva = models.ForeignKey('ppoa.Perspectiva', on_delete=models.CASCADE)
    iniciativa = models.CharField(
        max_length=500,
        null=False,
        blank=False
    )
    def __str__(self):
        return self.iniciativa

class UnidadGestion(models.Model):
    gestion = models.ForeignKey('gestion.Gestion', on_delete=models.CASCADE)
    unidad = models.OneToOneField('gestion.Unidad', on_delete=models.CASCADE)
    area = models.OneToOneField('ppoa.Area', on_delete=models.CASCADE)
    estrategia = ChainedForeignKey(
		'ppoa.Estrategia',
		chained_field='area',
		chained_model_field='area',
		show_all=False,
		auto_choose=True,
		sort=True
	)
    objetivoestrategico = ChainedForeignKey(
		'ppoa.ObjetivoEstrategico',
		chained_field='estrategia',
		chained_model_field='estrategia',
		show_all=False,
		auto_choose=True,
		sort=True
	)
    perspectiva = ChainedForeignKey(
		'ppoa.Perspectiva',
		chained_field='objetivoestrategico',
		chained_model_field='objetivoestrategico',
		show_all=False,
		auto_choose=True,
		sort=True
	)
    iniciativapdi = ChainedForeignKey(
		'ppoa.IniciativaPDI',
		chained_field='perspectiva',
		chained_model_field='perspectiva',
		show_all=False,
		auto_choose=True,
		sort=True
	)
    def media_inicitica(self):
        return Iniciativa.objects.filter(unidadgestion=self).aggregate(media=Avg('porcentaje'))['media']
    def __str__(self):
        return str(self.unidad)

class Iniciativa(models.Model):
    unidadgestion = models.ForeignKey('ppoa.UnidadGestion', on_delete=models.CASCADE)
    presupuesto = models.IntegerField(
        null=False,
        blank=False
    )
    f_inicio = models.DateField(
        verbose_name='Fecha de Inicio',
        null=False,
        blank=False
    )
    f_fin = models.DateField(
        verbose_name='Fecha de Finalisacion',
        null=False,
        blank=False
    )
    iniciativa = models.TextField(
        null=False,
        blank=False
    )
    i_objetivo = models.TextField(
        null=False,
        blank=False
    )
    actividad = models.CharField(
        max_length=2,
        null=False,
        blank=False,
        choices=(
            ('po','Politica'),
            ('pl','Plan'),
            ('pr','Proyecto'),
            ('pa','Programa'),
            ('a','Actividad'),
            ('t','Tarea')
        )
    )
    r_operativo = models.TextField(
        verbose_name='Responsable Operativo',
        null=False,
        blank=False
    )
    i_indices = models.TextField(
        verbose_name='Indicadores/Indices',
        null=False,
        blank=False
    )
    resultados = models.TextField(
        null=False,
        blank=False
    )
    condicionantes = models.TextField(
        null=False,
        blank=False
    )
    recurrente = models.BooleanField(
        null=False,
        blank=False,
        default=False
    )
    medio_verificacion = models.TextField(
        verbose_name='Medio de Verificacion',
        null=True,
        blank=True
    )
    porcentaje = models.PositiveIntegerField(
        null=False,
        blank=False,
        default=0,
        validators=[
            RegexValidator(
                regex = r'^(([0-9]{1})|([1-9][0-9]|100))$',
                message = 'Solo se permiten numeros del 0 al 100',
                code='0001'
            )
        ]
    )
    observacion = models.TextField(
        verbose_name='Obervaciones y Justificaion',
        null=True,
        blank=True
    )
    def __str__(self):
        return self.iniciativa
