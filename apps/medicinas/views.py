# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import (
	TemplateView, ListView
)
from django.shortcuts import render
from .models import *
from django.http import HttpResponse, Http404, HttpResponseRedirect 

def buscar(request):
	if 'busca' in request.GET and request.GET['busca']:
		consulta = request.GET['busca']
		#Acá me faltó importar los modelos de la app Medicinas. El problema que tengo es que no me deja importarlo y por eso es que no funciona la búsqueda.
		#El resto de la web funciona bárbaro. 

		aceitesBusq = AceiteCannabis.objects.filter(nombre__icontains=aceites)
		return render(request, 'medicinas/resultados.html', {'aceites': aceites,'query': consulta})
	else:
		return HttpResponseRedirect('/')


class ParchesView(ListView):
	template_name = "medicinas/parches.html"
	model = ParcheCannabis
	context_object_name = 'parches'

class AceitesView(ListView):
	template_name = "medicinas/aceites.html"
	model = AceiteCannabis
	context_object_name = 'aceites'

class CremasView(ListView):
	template_name = "medicinas/cremas.html"
	model = CremaCannabis
	context_object_name = 'cremas'

class PastillasView(ListView):
	template_name = "medicinas/pastillas.html"
	model = PastillaCannabis
	context_object_name = 'pastillas'

class PlantasView(ListView):
	template_name = "medicinas/plantas.html"
	model = PlantaMasticable
	context_object_name = 'plantas'

class CuidadoView(ListView):
	template_name = "medicinas/cuidado.html"
	model = CuidadoCannabis
	context_object_name = 'cuidado'
# Create your views here.
