# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Marcas(models.Model):
	nombre = models.CharField('Marca', max_length=15)

	def __str__(self):
		return self.nombre

class CuidadoCannabis(models.Model):
	nombrep = models.CharField('Nombre Planta', max_length=500)
	metodo = models.TextField('Metodo', max_length=500)
	ambiente = models.TextField('Ambiente mas favorable', max_length=500)
	productos = models.TextField('productos que puede utilizar', max_length=500)
	

	def __str__ (self):
		return self.nombrep
	#Falta el ForeingKey asociado a las plantas y la imagen 


class AceiteCannabis(models.Model):
	nombre = models.CharField('Nombre aceite',max_length=50)
	resena = models.TextField('Reseña sobre el aceite', max_length=500)
	mdu = models.TextField('Modo de uso', max_length=150)
	ES = models.CharField('Efectos secundarios', max_length=150)
	Precio = models.CharField('Precio', max_length=10) 
	Importador = models.CharField('Importador', max_length=20)




	#Falta el ForeingKey y la imagen 

	def __str__(self):
		return self.nombre

class CremaCannabis(models.Model):
	resena = models.TextField('Reseña sobre la crema', max_length=300)
	mdu = models.TextField('Modo de uso', max_length=100)
	ES = models.CharField('Efectos secundarios', max_length=10)
	Precio = models.CharField('Precio', max_length=5)

	#Falta ForeignKey para la marca e Imagen

	def __str__(self):
		return self.resena

class ParcheCannabis(models.Model):
	resena = models.TextField('Reseña sobre el parche', max_length=300)
	mdu = models.TextField('Modo de uso', max_length=100)
	ES = models.CharField('Efectos secundarios', max_length=10)
	Precio = models.CharField('Precio', max_length=5)

	#Falta ForeignKey para la marca e Imagen

	def __str__(self):
		return self.resena	


class PlantaMasticable(models.Model):
	nombre = models.CharField('Nombre planta',max_length=50)
	resena = models.TextField('Reseña sobre la planta', max_length=150)
	mdu = models.TextField('Modo de uso', max_length=150)
	ES = models.CharField('Efectos secundarios', max_length=150)
	Precio = models.CharField('Precio', max_length=10) 
	Importador = models.CharField('Importador', max_length=20)
	
	#Falta el ForeingKey y la imagen 

	def __str__(self):
		return self.nombre


class PastillaCannabis(models.Model):
	nombre = models.CharField('Nombre pastilla',max_length=50)
	resena = models.TextField('Reseña sobre la pastilla', max_length=150)
	mdu = models.TextField('Modo de uso', max_length=150)
	ES = models.CharField('Efectos secundarios', max_length=150)
	Precio = models.CharField('Precio', max_length=10) 
	Importador = models.CharField('Importador', max_length=20)
	#Falta el ForeingKey y la imagen 

	def __str__(self):
		return self.nombre
# Create your models here.
