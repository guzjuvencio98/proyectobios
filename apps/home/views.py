# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import (
	TemplateView,
)
from django.core.mail import send_mail 
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
from django.http import HttpResponse, Http404, HttpResponseRedirect 
from django.views.defaults import page_not_found



# Una vista procesa el dato y renderiza el resultado en pantalla
# Siempre nos pide un template con el cual trabajar 
# Un template es generalmente es un archivo HTML

def inicio(request):
	return render(request, "home/index.html", {})

def nosotros(request):
	return render(request, "home/nosotros.html", {})

def contacto(request):
	if request.method == 'POST':
		mensaje = request.POST['Mensaje']

		send_mail('Mensaje enviado desde CannabisSTORE', 
			mensaje, 
			settings.EMAIL_HOST_USER, 
			['cannabisstore.uy@gmail.com'], 
			fail_silently=False)
	return render(request, "home/contacto.html", {})

def usuarionuevo(request):
	if request.method == 'POST': 
		formulario = UserCreationForm(request.POST)
		if formulario.is_valid:
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario = UserCreationForm()
	context = {'formulario': formulario}
	return render(request, 'home/usuarionuevo.html', context)

			
def ingresar(request):
	if not request.user.is_anonymous():
		return HttpResponseRedirect('/privado')
	if request.method == 'POST':
		formulario = AuthenticationForm(request.POST)
		if formulario.is_valid:
			usuario = request.POST['username']
			clave = request.POST['password']
			acceso = authenticate(username=usuario, password=clave)
			if acceso is not None:
				if acceso.is_active:
					login(request, acceso)
					return HttpResponseRedirect('/privado')
				else:
					return render(request, 'home/noactivo.html')
			else:
				return render(request, 'home/nousuario.html')
	else:
		formulario = AuthenticationForm()
	context = {'formulario': formulario}
	return render(request, 'home/ingresar.html', context)

login_required(login_url='/ingresar')
def privado(request):
	usuario = request.user
	context = {'usuario': usuario}
	return render(request, 'home/privado.html', context)


def cerrar(request):
	if not request.user.is_anonymous():
		logout(request)
		return HttpResponseRedirect('/')
	else:
		return render(request, 'home/nologueado.html')

def buscar(request):
	if 'busca' in request.GET and request.GET['busca']:
		consulta = request.GET['busca']
		#Acá me faltó importar los modelos de la app Medicinas. El problema que tengo es que no me deja importarlo y por eso es que no funciona la búsqueda.
		#El resto de la web funciona bárbaro. 

		aceites = AceiteCannabis.objects.filter(nombre__icontains=aceites)
		return render(request, 'medicinas/resultados.html', {'aceites': aceites,'query': consulta})
	else:
		return HttpResponseRedirect('/')

def error(request):
	plantilla = '404.html'
	return page_not_found(request, template_name=plantilla)

class IndexView(TemplateView):
	template_name = "home/index.html"

# Create your views here.
