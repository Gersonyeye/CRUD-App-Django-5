from django.db import models

# Create your models here.

class Usuarios(models.Model):
    cedula = models.IntegerField(primary_key=True,
                                 unique=True
                                 )
    nombre = models.CharField(max_length=250 
                              )
    apellido= models.CharField(max_length=250
                             )
    correo = models.EmailField()
    