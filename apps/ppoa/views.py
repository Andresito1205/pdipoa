from statistics import mode
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, FormView, DeleteView, DetailView
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.urls import reverse_lazy
from .forms import *
from .models import *
from apps.users.forms import SearchForm
from constance import config
from django.apps import apps
from django_weasyprint import WeasyTemplateResponseMixin
from apps.users.generic import *

# Create your views here.
class AreaListView(ListView):
    model = Area
    paginate_by = 10
    form_class = SearchForm
    template_name = 'area/area_list.html'
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
                Q(unidad__nombre__icontains=self.search)|
                Q(nombre__icontains=self.search),
                gestion__gestion=config.GESTION_ACTIVA
            )
        else:
            return self.model.objects.filter(gestion__gestion=config.GESTION_ACTIVA)

class AreaCreateView(CreateView):
    form_class = AreaForm
    template_name = 'area/area_create.html'
    success_url = reverse_lazy('ppoa:area_list')
    def form_valid(self, form):
        form.instance.gestion = apps.get_model('gestion','Gestion').objects.get(gestion=config.GESTION_ACTIVA)
        return super().form_valid(form)

class AreaUpdateView(UpdateView):
    model = Area
    form_class = AreaForm
    template_name = 'area/area_update.html'
    success_url = reverse_lazy('ppoa:area_list')

#estrategia
class EstrategiaListView(ListView):
    model = Estrategia
    paginate_by = 10
    form_class = SearchForm
    template_name = 'estrategia/estrategia_list.html'
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
                Q(codigo_foda__icontains=self.search)|
                Q(estrategia__icontains=self.search),
                area__id=self.kwargs['pk']
            )
        else:
            return self.model.objects.filter(area__id=self.kwargs['pk'])

class EstrategiaCreateView(CreateView):
    model_extra = Area
    form_class = EstrategiaForm
    template_name = 'estrategia/estrategia_create.html'
    success_url = 'ppoa:estrategia_list'
    def form_valid(self, form):
        form.instance.area = self.model_extra.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)
    def get_success_url(self):
        return reverse_lazy(self.success_url, kwargs={'pk':self.object.area_id})

class EstrategiaUpdateView(UpdateView):
    model = Estrategia
    form_class = EstrategiaForm
    template_name = 'estrategia/estrategia_update.html'
    success_url = 'ppoa:estrategia_list'
    def get_success_url(self):
        return reverse_lazy(self.success_url, kwargs={'pk':self.object.area_id})

#objetivo estrategico
class ObjetivoEstrategicoListView(ListView, ModelExtraView):
    model_extra = Estrategia
    model = ObjetivoEstrategico
    paginate_by = 10
    form_class = SearchForm
    template_name = 'objetivoestrategico/objetivoestrategico_list.html'
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
                Q(objetivo__icontains=self.search),
                estrategia__id=self.kwargs['pk']
            )
        else:
            return self.model.objects.filter(estrategia__id=self.kwargs['pk'])

class ObjetivoEstrategicoCreateView(CreateView):
    model_extra = Estrategia
    form_class = ObjetivoEstrategicoForm
    template_name = 'objetivoestrategico/objetivoestrategico_create.html'
    success_url = 'ppoa:oestrategico_list'
    def form_valid(self, form):
        form.instance.estrategia = self.model_extra.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)
    def get_success_url(self):
        return reverse_lazy(self.success_url, kwargs={'pk':self.object.estrategia_id})

class ObjetivoEstrategicoUpdateView(UpdateView):
    model = ObjetivoEstrategico
    form_class = ObjetivoEstrategicoForm
    template_name = 'objetivoestrategico/objetivoestrategico_update.html'
    success_url = 'ppoa:oestrategico_list'
    def get_success_url(self):
        return reverse_lazy(self.success_url, kwargs={'pk':self.object.estrategia_id})

#perspectiva
class PerspectivaListView(ListView, ModelExtraView):
    model_extra = ObjetivoEstrategico
    model = Perspectiva
    paginate_by = 10
    form_class = SearchForm
    template_name = 'perspectiva/perspectiva_list.html'
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
                Q(codigo__icontains=self.search)|
                Q(perspectiva__icontains=self.search),
                objetivoestrategico__id=self.kwargs['pk']
            )
        else:
            return self.model.objects.filter(objetivoestrategico__id=self.kwargs['pk'])

class PerspectivaCreateView(CreateView):
    model_extra = ObjetivoEstrategico
    form_class = PerspectivaForm
    template_name = 'perspectiva/perspectiva_create.html'
    success_url = 'ppoa:perspectiva_list'
    def form_valid(self, form):
        form.instance.objetivoestrategico = self.model_extra.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)
    def get_success_url(self):
        return reverse_lazy(self.success_url, kwargs={'pk':self.object.objetivoestrategico_id})

class PerspectivaUpdateView(UpdateView):
    model = Perspectiva
    form_class = PerspectivaForm
    template_name = 'perspectiva/perspectiva_update.html'
    success_url = 'ppoa:perspectiva_list'
    def get_success_url(self):
        return reverse_lazy(self.success_url, kwargs={'pk':self.object.objetivoestrategico_id})

#IniciativaPDIForm
class IniciativaPDIListView(ListView, ModelExtraView):
    model_extra = Perspectiva
    model = IniciativaPDI
    paginate_by = 10
    form_class = SearchForm
    template_name = 'iniciativapdi/iniciativapdi_list.html'
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
                Q(iniciativa__icontains=self.search),
                perspectiva__id=self.kwargs['pk']
            )
        else:
            return self.model.objects.filter(perspectiva__id=self.kwargs['pk'])

class IniciativaPDICreateView(CreateView):
    model_extra = Perspectiva
    form_class = IniciativaPDIForm
    template_name = 'iniciativapdi/iniciativapdi_create.html'
    success_url = 'ppoa:iniciativapdi_list'
    def form_valid(self, form):
        form.instance.perspectiva = self.model_extra.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)
    def get_success_url(self):
        return reverse_lazy(self.success_url, kwargs={'pk':self.object.perspectiva_id})

class IniciativaPDIUpdateView(UpdateView):
    model = IniciativaPDI
    form_class = IniciativaPDIForm
    template_name = 'iniciativapdi/iniciativapdi_update.html'
    success_url = 'ppoa:iniciativapdi_list'
    def get_success_url(self):
        return reverse_lazy(self.success_url, kwargs={'pk':self.object.perspectiva_id})

#unidad gest
class UnidadGestionListView(ListView):
    model = UnidadGestion
    paginate_by = 10
    form_class = SearchForm
    template_name = 'undiadgest/undiadgest_list.html'
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
                Q(unidad__nombre__icontains=self.search),
                gestion__gestion=config.GESTION_ACTIVA
            )
        else:
            return self.model.objects.filter(gestion__gestion=config.GESTION_ACTIVA)

class UnidadGestionCreateView(CreateView):
    form_class = UnidadGestionForm
    template_name = 'undiadgest/undiadgest_create.html'
    success_url = reverse_lazy('ppoa:unidadg_list')
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['gestiona'] = config.GESTION_ACTIVA
        return kwargs
    def form_valid(self, form):
        form.instance.gestion = apps.get_model('gestion','Gestion').objects.get(gestion=config.GESTION_ACTIVA)
        return super().form_valid(form)

class UnidadGestionUpdateView(UpdateView):
    model = UnidadGestion
    form_class = UnidadGestionForm
    template_name = 'undiadgest/undiadgest_update.html'
    success_url = reverse_lazy('ppoa:unidadg_list')
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['gestiona'] = config.GESTION_ACTIVA
        return kwargs

#iniciativa POA
class UnidadIniciativaListView(ListView):
    model = Iniciativa
    paginate_by = 10
    form_class = SearchForm
    template_name = 'iniciativa/iniciativa_list.html'
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
                Q(iniciativa__icontains=self.search)|
                Q(i_objetivo__icontains=self.search),
                unidadgestion__id=self.kwargs['pk']
            )
        else:
            return self.model.objects.filter(unidadgestion__id=self.kwargs['pk'])

class UnidadIniciativaCreateView(CreateView):
    model_extra = UnidadGestion
    form_class = IniciativaForm
    template_name = 'iniciativa/iniciativa_create.html'
    success_url = 'ppoa:iniciativa_list'
    def form_valid(self, form):
        form.instance.unidadgestion = self.model_extra.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)
    def get_success_url(self):
        return reverse_lazy(self.success_url, kwargs={'pk':self.object.unidadgestion_id})

class UnidadIniciativaUpdateView(UpdateView):
    model = Iniciativa
    form_class = IniciativaForm
    template_name = 'iniciativa/iniciativa_update.html'
    success_url = 'ppoa:iniciativa_list'
    def get_success_url(self):
        return reverse_lazy(self.success_url, kwargs={'pk':self.object.unidadgestion_id})

class ReporteGestionDetailView(DetailView):
    model = apps.get_model('gestion','Gestion')
    template_name = 'reportes/gestion.html'
    def get_object(self, queryset=None):
        return self.model.objects.get(gestion=config.GESTION_ACTIVA)

class PDFReporteGestionDetailView(WeasyTemplateResponseMixin, ReporteGestionDetailView):
    pass