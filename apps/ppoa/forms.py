from django import forms
from django.apps import apps
from constance import config
from .models import *

class Html5DateInput(forms.DateInput):
	input_type = 'date'
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.format = ('%Y-%m-%d')

class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        exclude = ['gestion']

class EstrategiaForm(forms.ModelForm):
    class Meta:
        model = Estrategia
        exclude = ['area']

class ObjetivoEstrategicoForm(forms.ModelForm):
    class Meta:
        model = ObjetivoEstrategico
        exclude = ['estrategia']

class PerspectivaForm(forms.ModelForm):
    class Meta:
        model = Perspectiva
        exclude = ['objetivoestrategico']

class IniciativaPDIForm(forms.ModelForm):
    class Meta:
        model = IniciativaPDI
        exclude = ['perspectiva']

class UnidadGestionForm(forms.ModelForm):
    class Meta:
        model = UnidadGestion
        exclude = ['gestion']
    def __init__(self, *args, **kwargs):
        gestiona = kwargs.pop('gestiona', None)
        print(gestiona)
        super().__init__(*args, **kwargs)
        self.fields['area'].queryset = Area.objects.filter(gestion__gestion=gestiona)

class IniciativaForm(forms.ModelForm):
    class Meta:
        model = Iniciativa
        exclude = ['unidadgestion','medio_verificacion','porcentaje','observacion']
        widgets = {
			'f_inicio':Html5DateInput(),
			'f_fin':Html5DateInput()
		}
