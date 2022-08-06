"""sistema_pesquero URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.urls import path,include
from django.contrib import admin
from django.urls import path

from front.views.index import index 
from front.views.reportes.index_view import IndexView as ReporteIndex
from front.views.usuarios.index import IndexView as UsuariosIndex
from front.views.usuarios.registro import CrearView as UserCrearView
from front.views.usuarios.registro import ActualizarView as UserActualizarView
from front.views.viaje.registro import RegistroView as ViajeRegistroView

from django.contrib.auth.decorators import login_required

urls_front = [
    path('', index),
    path('reportes', login_required(ReporteIndex.as_view()) ),
    path('reportes/index', login_required(ReporteIndex.as_view()) ),
    path('reportes/index/<id>/', login_required(ReporteIndex.as_view()) ),
    path('reportes/viaje/editar/<id>/', login_required(ViajeRegistroView.as_view()) ),
    path('usuarios/', login_required(UsuariosIndex.as_view()), name="usuarios" ),
    path('usuarios/crear/', login_required(UserCrearView.as_view()) ),
    path('usuarios/crear/<pk>', login_required(UserActualizarView.as_view()) ),
]