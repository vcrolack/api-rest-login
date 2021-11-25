from django.db import models

# Create your models here.
class User(models.Model):
  name = models.CharField(max_length=50, verbose_name="Nombre")
  lastname = models.CharField(max_length=50, verbose_name="Apellido")
  username = models.CharField(max_length=50, verbose_name="Nombre de usuario")
  email = models.CharField(verbose_name="Correo electrónico", max_length=50)
  password = models.CharField(max_length=25, verbose_name= "Contraseña")

class Bike(models.Model):
  nameBike = models.CharField(max_length=50, verbose_name="nombre bicicleta")
  price = models.IntegerField()
  description = models.TextField()
  imgUrl = models.TextField()
