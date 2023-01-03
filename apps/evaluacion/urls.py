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

from apps.users.models import Permisos
from .views import *

urlpatterns = [
    path('unidadese/', permission_required('users.evaluacion')(login_required(UnidadGestionEView.as_view())), name='unidadese'),
    path('iniciativae/<int:pk>/', permission_required('users.evaluacion')(login_required(UpdateIniciativaEView.as_view())), name='iniciativae'),

    path('reporteeval/', permission_required('users.evaluacion')(login_required(PDFReporteEvaluacionDetailView.as_view())), name="reporte_evaluacion")
]
