from django import forms
from django.apps import apps

class IniciativaEForm(forms.ModelForm):
    class Meta:
        model = apps.get_model('ppoa','Iniciativa')
        fields = ['porcentaje','observacion']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['porcentaje'].required = True
        self.fields['observacion'].required = True
