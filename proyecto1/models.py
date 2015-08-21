from django.db import models
# Amadeus was here 2
# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        db_table = 'Usuario'

