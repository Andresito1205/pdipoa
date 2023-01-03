from django import forms
from .models import *
from constance import config

class search_form(forms.Form):
	search = forms.CharField(required=False ,label="", help_text="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Buscar...'}))

class GestionForm(forms.ModelForm):
    class Meta:
        model = Gestion
        exclude = ['']
        #fields = ['']

class UnidadForm(forms.ModelForm):
    class Meta:
        model = Unidad
        exclude = ['gestion']

class GestionActivaForm(forms.Form):
    gestion = forms.IntegerField(required=True, initial=lambda:config.GESTION_ACTIVA)
    def save(self):
        gestion = self.cleaned_data['gestion']
        config.GESTION_ACTIVA = gestion
        return
