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
from django.contrib import admin
from django.urls import path
from django.urls.conf import include, include
from django.views.generic import RedirectView
from django.urls import reverse_lazy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chaining/', include('smart_selects.urls')),
    path('',RedirectView.as_view(url=reverse_lazy('users:main')), name='home'),
    path('users/', include(('apps.users.urls','users'), namespace='users')),
    path('gestion/', include(('apps.gestion.urls','gestion'), namespace='gestion')),
    path('ppoa/', include(('apps.ppoa.urls','ppoa'), namespace='ppoa')),
    path('evaluacion/', include(('apps.evaluacion.urls','evaluacion'), namespace='evaluacion'))
]
