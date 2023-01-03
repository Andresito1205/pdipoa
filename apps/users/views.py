from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, FormView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import CharField, Q, Count
from django.db.models.functions import Cast
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from apps.gestion.forms import search_form
from .models import *
from .forms import *

# Create your views here.

def main(request):
    return render(request,'main.html',{})

class CreateUserView(CreateView):
	form_class = CreateUserForm
	template_name = 'users/create_user.html'
	success_url = reverse_lazy('users:usuarios_list')
	success_message = 'El usuario se creo correctamente'

class UserListView(ListView):
	model = User
	paginate_by = 10
	form_class = search_form
	template_name = 'users/list_users.html'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.form_class()
		if self.request.GET:
			context['form'] = self.form_class(self.request.GET)
		return context
	def get(self, *args, **kwargs):
		self.search = None
		if self.request.method == "GET" and 'search' in self.request.GET:
			form = self.form_class(self.request.GET)
			if form.is_valid():
				self.search = form.cleaned_data['search']
				if self.search=='':
					return HttpResponseRedirect(self.request.path)
		return super().get(*args, **kwargs)
	def get_queryset(self):
		if self.search:
			return super().get_queryset().filter(
				Q(id__icontains=self.search)|
				Q(username__icontains=self.search)|
				Q(first_name__icontains=self.search)|
				Q(last_name__icontains=self.search)|
				Q(email__icontains=self.search),
				is_staff=False,
			)
		else:
			return super().get_queryset().filter(is_staff=False)
		

class UpdateUserFromUserView(UpdateView):
	model = User
	form_class = UpdateUserForm
	template_name = 'users/update_user_from_user.html'
	success_url = '/'
	success_message = 'Su información fue actualizada con éxito'
	def get_object(self, queryset=None):
		return self.request.user

class PermisosView(FormView):
	model = User
	model_permissions = Permisos
	form_class = AddPermissionsForm
	template_name = 'users/permisos.html'
	success_url = reverse_lazy('users:usuarios_list')
	def get_form_kwargs(self):
		kwargs = super().get_form_kwargs()
		kwargs['model_permissions'] = self.model_permissions
		return kwargs
	def get_initial(self):
		pk = self.kwargs['pk']
		self.user = self.model.objects.get(id=pk)
		content_type = ContentType.objects.get_for_model(self.model_permissions)
		permisos_actuales = self.user.user_permissions.filter(content_type=content_type)
		perms = {}
		for p in permisos_actuales:
			perms[p.codename] = True
		return perms
		#return { 'usuarios': True, 'academico': False }
	def form_valid(self, form):
		if form.is_valid():
			data = form.cleaned_data
			for p in data:
				content_type=ContentType.objects.get_for_model(self.model_permissions)
				permission = Permission.objects.get(content_type=content_type, codename=p)
				if data[p]:
					self.user.user_permissions.add(permission)
				else:
					self.user.user_permissions.remove(permission)
		return super().form_valid(form)
    