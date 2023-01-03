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
from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required
from .views import *

urlpatterns = [
    path('gestioncreate/', permission_required('users.gestion')(login_required(GestionCreateView.as_view())), name='gestion_create'),
    path('gestionlist/',permission_required('users.gestion')(login_required(GetionListaView.as_view())), name='gestion_list'),
    path('gestionupdate/<int:pk>/', permission_required('users.gestion')(login_required(GetsionUpdateView.as_view())), name='gestion_update'),
    path('gestiondelete/<int:pk>/', permission_required('users.gestion')(login_required(GestionDeleteView.as_view())), name='gestion_delete'),

    path('unidadlist/', permission_required('users.gestion')(login_required(UnidadListaView.as_view())), name='unidad_list'),
    path('createunidad/', permission_required('users.gestion')(login_required(CreateUnidadView.as_view())), name='unidad_create'),
    path('updateunidad/<int:pk>/', permission_required('users.gestion')(login_required(UpdateUnidadView.as_view())), name='unidad_update'),

    path('gestionactiva/', permission_required('users.gestion')(login_required(GestionActivaView.as_view())), name='gestion_activa')
]
