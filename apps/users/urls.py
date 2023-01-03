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
from django.contrib.auth.views import LoginView, logout_then_login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from .views import *

urlpatterns = [
    path('', login_required(main), name='main'),
    path('login/',
        LoginView.as_view(template_name='auth/login.html'),
        name='login'
    ),
    path('logout/',
        logout_then_login,
        name='logout'
    ),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='auth/password_reset.html', email_template_name='auth/password_reset_email.html', subject_template_name='auth/password_reset_subject.txt', success_url=reverse_lazy('users:password_reset_done')), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='auth/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='auth/password_reset_confirm.html',success_url=reverse_lazy('users:password_reset_complete')), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='auth/password_change_done.html'), name='password_reset_complete'),

    path('updateuserfuser/', login_required(UpdateUserFromUserView.as_view()), name='update_user_user'),
    path('createuser/', permission_required('users.users')(login_required(CreateUserView.as_view())), name='usuarios_create'),
    path('usuarioslist/', permission_required('users.users')(login_required(UserListView.as_view())), name='usuarios_list'),
    path('permisos/<int:pk>/', permission_required('users.users')(login_required(PermisosView.as_view())), name='usuarios_perms')
]
