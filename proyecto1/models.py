from django.db import models
# Amadeus was here 2
# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    correo = models.CharField(max_length=200)
    fechaNacimiento = models.DateField()
    profesion = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    bloqueado = models.BooleanField(default=False)

    class Meta:
        db_table = 'Usuario'

class Afiliado(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        db_table = 'Afiliado'
