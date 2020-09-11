"""pmedicinales URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include, handler404
from django.contrib import admin
from apps.home import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.home.urls')),
    url(r'^', include('apps.medicinas.urls')),
    url(r'^$', views.inicio, name='inicio'),
    url(r'^contacto/', views.contacto, name='contacto'),
    url(r'^nosotros/', views.nosotros, name='nosotros'),
    url(r'^registrar/', views.usuarionuevo, name='registrar'),
    url(r'^ingresar/', views.ingresar, name='ingresar'),
    url(r'^privado/', views.privado, name='privado'),
    url(r'^cerrar/', views.cerrar, name='cerrar'),
    url(r'^buscar/', views.buscar, name='buscar'),
]

