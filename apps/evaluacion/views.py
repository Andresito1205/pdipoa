from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, FormView, DeleteView, DetailView
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.urls import reverse_lazy
from apps.users.forms import SearchForm
from django.apps import apps
from constance import config
from django_weasyprint import WeasyTemplateResponseMixin
from .forms import *

# Create your views here.
class UnidadGestionEView(ListView):
    model = apps.get_model('ppoa','UnidadGestion')
    paginate_by = 10
    form_class = SearchForm
    template_name = 'unidadg/uniadag_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'gestion' not in context:
            context['gestion'] = apps.get_model('gestion','Gestion').objects.get(gestion=config.GESTION_ACTIVA)
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
                Q(unidad__nombre__icontains=self.search)|
                Q(nombre__icontains=self.search),
                gestion__gestion=config.GESTION_ACTIVA
            )
        else:
            return self.model.objects.filter(gestion__gestion=config.GESTION_ACTIVA)

class UpdateIniciativaEView(UpdateView):
    model = apps.get_model('ppoa','Iniciativa')
    form_class = IniciativaEForm
    template_name = 'iniciativae/iniciativae_update.html'
    success_url = reverse_lazy('evaluacion:unidadese')

class ReporteEvaluacionDetailView(DetailView):
    model = apps.get_model('gestion','Gestion')
    template_name = 'reportes/evaluacion.html'
    def get_object(self, queryset=None):
        return self.model.objects.get(gestion=config.GESTION_ACTIVA)

class PDFReporteEvaluacionDetailView(WeasyTemplateResponseMixin, ReporteEvaluacionDetailView):
    pass