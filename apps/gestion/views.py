from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, FormView, DeleteView
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.urls import reverse_lazy
from .forms import *
from .models import *

# Create your views here.

class GestionCreateView(CreateView):
    form_class = GestionForm
    template_name = 'gestion/gestion_create.html'
    success_url = reverse_lazy('gestion:gestion_list')

class GetionListaView(ListView):
    model = Gestion
    form_class = search_form
    paginate_by = 10
    template_name = 'gestion/gestion_list.html'
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
        if(self.search):
            return self.model.objects.filter(
                Q(id__icontains=self.search)|
                Q(gestion__icontains=self.search)
            )
        else:
            return super().get_queryset()

class GetsionUpdateView(UpdateView):
    model = Gestion
    form_class = GestionForm
    template_name = 'gestion/gestion_update.html'
    success_url = reverse_lazy('gestion:gestion_list')

class GestionDeleteView(DeleteView):
    model = Gestion
    form_class = GestionForm
    template_name = 'gestion/gestion_delete.html'
    success_url = reverse_lazy('gestion:gestion_list')

#Unidades
class CreateUnidadView(CreateView):
    model_extra = Gestion
    form_class = UnidadForm
    template_name = 'unidad/unidad_create.html'
    success_url = reverse_lazy('gestion:unidad_list')

class UnidadListaView(ListView):
    model = Unidad
    paginate_by = 10
    form_class = search_form
    template_name = 'unidad/unidad_list.html'
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
        if(self.search):
            return self.model.objects.filter(
                Q(id__icontains=self.search)|
                Q(nombre__icontains=self.search)
            )
        else:
            return self.model.objects.filter()
            #return self.model.objects.filter(gestion__gestion=2012)

class UpdateUnidadView(UpdateView):
    model = Unidad
    form_class = UnidadForm
    template_name = 'unidad/unidad_update.html'
    success_url = reverse_lazy('gestion:unidad_list')

class GestionActivaView(FormView):
    form_class = GestionActivaForm
    template_name = 'gestion_activa.html'
    success_url = '/'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
