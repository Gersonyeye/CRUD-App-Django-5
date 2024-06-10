from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Usuarios(models.Model):
    cedula = models.IntegerField(primary_key=True,
                                 unique=True
                                 )
    nombre = models.CharField(max_length=250,
                              validators = [RegexValidator(r"^[A-Za-záéíóúÁÉÍÓÚñÑüÜ]+$")]
                              )
    apellido= models.CharField(max_length=250,
                              validators = [RegexValidator(r"^[A-Za-záéíóúÁÉÍÓÚñÑüÜ]+$")]
                              )
    correo = models.EmailField()
    