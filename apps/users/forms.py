from django import forms
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class SearchForm(forms.Form):
	search = forms.CharField(required=False, label="", help_text="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Buscar...','autocomplete':'off'}))

class CreateUserForm(UserCreationForm):
	class Meta:
		model=User
		fields=[
			'username',
			'first_name',
			'last_name',
			'email'
		]
	def __init__(self, *args, **kwargs):
		super(CreateUserForm, self).__init__(*args, **kwargs)
		self.fields['email'].required = True
		self.fields['first_name'].required = True
		self.fields['last_name'].required = True
        

class UpdateUserForm(forms.ModelForm):
	class Meta:
		model=User
		fields=[
			'first_name',
			'last_name',
			'email'
		]
		labels= {
			'first_name':'Nombre(s)',
			'last_name':'Apellido(s)',
		}
	def __init__(self, *args, **kwargs):
		super(UpdateUserForm, self).__init__(*args, **kwargs)
		self.fields['email'].required = True
		self.fields['first_name'].required = True
		self.fields['last_name'].required = True

class AddPermissionsForm(forms.Form):
	def __init__(self, *args, **kwargs):
		#esto permite aderir datos al constructor dinamicamente deste arg y kwargs
		model_permissions = kwargs.pop('model_permissions', None)
		showd_permissions = kwargs.pop('showd_permissions', False)
		super(AddPermissionsForm, self).__init__(*args, **kwargs)
		content_type=ContentType.objects.get_for_model(model_permissions)
		permission = Permission.objects.filter(content_type=content_type).order_by('id')
		for idx, p in enumerate(permission):
			if(showd_permissions):
				self.fields[p.codename] = forms.BooleanField(label='Dar permiso para el modulo: '+ str(p.name), required=False)
			else:
				if(idx>3):
					self.fields[p.codename] = forms.BooleanField(label='Dar permiso para el modulo: '+ str(p.name), required=False)
