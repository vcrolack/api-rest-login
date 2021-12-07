from django.db import models

# Create your models here.
class User(models.Model):
  name = models.CharField(max_length=50, verbose_name="Nombre")
  lastname = models.CharField(max_length=50, verbose_name="Apellido")
  username = models.CharField(max_length=50, verbose_name="Nombre de usuario")
  email = models.CharField(verbose_name="Correo electrónico", max_length=50)
  password = models.CharField(max_length=25, verbose_name= "Contraseña")
  isDriver = models.CharField(max_length=10, verbose_name="Conductor")

class Bike(models.Model):
  nameBike = models.CharField(max_length=50, verbose_name="nombre bicicleta")
  price = models.IntegerField()
  description = models.TextField()
  imgUrl = models.TextField()

class Vehicle(models.Model):
  patent = models.CharField(max_length=6, verbose_name="patente", primary_key=True)
  brand = models.CharField(max_length=30, verbose_name="Marca")
  model = models.CharField(max_length=30, verbose_name="Modelo")
  capacity = models.IntegerField(verbose_name="Capacidad")
  year = models.IntegerField(verbose_name="Anio")
  user_id =  models.IntegerField(verbose_name="Id usuario", blank=False, null=False)
  

class Route(models.Model):
  campus = models.CharField(max_length=30,verbose_name="Sede")
  destiny = models.CharField(max_length=60, verbose_name="Destino") 
  rate = models.IntegerField(verbose_name="Tarifa")
  user_id = models.IntegerField(verbose_name="Id usuario")
  passengers_suscribed = models.IntegerField(verbose_name="Pasajeros suscritos")