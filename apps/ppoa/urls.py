"""pdipoa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from cmath import log
from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required
from .views import *

urlpatterns = [
    path('arealist/', permission_required('users.ppoa')(login_required(AreaListView.as_view())), name='area_list'),
    path('areacreate/', permission_required('users.ppoa')(login_required(AreaCreateView.as_view())), name='area_create'),
    path('areaupdate/<int:pk>/', permission_required('users.ppoa')(login_required(AreaUpdateView.as_view())), name='area_update'),

    path('estrategialist/<int:pk>/', permission_required('users.ppoa')(login_required(EstrategiaListView.as_view())), name='estrategia_list'),
    path('estrategiacreate/<int:pk>/', permission_required('users.ppoa')(login_required(EstrategiaCreateView.as_view())), name='estrategia_create'),
    path('estrategiaupdate/<int:pk>/', permission_required('users.ppoa')(login_required(EstrategiaUpdateView.as_view())), name='estrategia_update'),

    path('oestrategicolist/<int:pk>/', permission_required('users.ppoa')(login_required(ObjetivoEstrategicoListView.as_view())), name='oestrategico_list'),
    path('oestrategicocreate/<int:pk>/', permission_required('users.ppoa')(login_required(ObjetivoEstrategicoCreateView.as_view())), name='oestrategico_create'),
    path('oestrategicoupdate/<int:pk>/', permission_required('users.ppoa')(login_required(ObjetivoEstrategicoUpdateView.as_view())), name='oestrategico_update'),

    path('perspectivalist/<int:pk>/', permission_required('users.ppoa')(login_required(PerspectivaListView.as_view())), name='perspectiva_list'),
    path('perspectivacreate/<int:pk>/', permission_required('users.ppoa')(login_required(PerspectivaCreateView.as_view())), name='perspectiva_create'),
    path('perspectivaupdate/<int:pk>/', permission_required('users.ppoa')(login_required(PerspectivaUpdateView.as_view())), name='perspectiva_update'),

    path('iniciativapdilist/<int:pk>/', permission_required('users.ppoa')(login_required(IniciativaPDIListView.as_view())), name='iniciativapdi_list'),
    path('iniciativapdicreate/<int:pk>/', permission_required('users.ppoa')(login_required(IniciativaPDICreateView.as_view())), name='iniciativapdi_create'),
    path('iniciativapdiupdate/<int:pk>/', permission_required('users.ppoa')(login_required(IniciativaPDIUpdateView.as_view())), name='iniciativapdi_update'),

    path('unidadglist/', permission_required('users.ppoa')(login_required(UnidadGestionListView.as_view())), name='unidadg_list'),
    path('unidadgcreate/', permission_required('users.ppoa')(login_required(UnidadGestionCreateView.as_view())), name='unidadg_create'),
    path('unidadgupdate/<int:pk>/', permission_required('users.ppoa')(login_required(UnidadGestionUpdateView.as_view())), name='unidadg_update'),

    path('iniciativalist/<int:pk>/', permission_required('users.ppoa')(login_required(UnidadIniciativaListView.as_view())), name='iniciativa_list'),
    path('iniciativacreate/<int:pk>/', permission_required('users.ppoa')(login_required(UnidadIniciativaCreateView.as_view())), name='iniciativa_create'),
    path('iniciativaupdate/<int:pk>/', permission_required('users.ppoa')(login_required(UnidadIniciativaUpdateView.as_view())), name='iniciativa_update'),

    path('reportegestion/', permission_required('users.ppoa')(login_required(PDFReporteGestionDetailView.as_view())), name='reporte_gestion')
]
