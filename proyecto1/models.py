from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        db_table = 'Usuario'


class Afiliado(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        db_table = 'Afiliado'
