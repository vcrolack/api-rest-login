from django.db import models

# Create your models here.
class User(models.Model):
  name = models.CharField(max_length=50, verbose_name="Nombre")
  lastname = models.CharField(max_length=50, verbose_name="Apellido")
  username = models.CharField(max_length=50, verbose_name="Nombre de usuario")
  email = models.EmailField(verbose_name="Correo electrónico")
  password = models.CharField(max_length=25, verbose_name= "Contraseña")
