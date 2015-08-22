from django.db import models
# Amadeus was here 2
# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    telefono = models.IntegerField()
    correo = models.EmailField()
    fechaNacimiento = models.DateField()
    profesion = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    bloqueado = models.BooleanField(default=False)

    class Meta:
        db_table = 'Usuario'

class AsignacionCuenta(models.Model):
    idUsuario = models.IntegerField()
    idCuenta = models.IntegerField()

    class Meta:
        db_table = 'AsignacionCuenta'

class Cuenta(models.Model):
    tipo = models.CharField(max_length=200)
    limite = models.FloatField()
    fechaCreacion = models.DateField()

    class Meta:
        db_table = 'Cuenta'

class AsignacionTarjeta(models.Model):
    idCuenta = models.IntegerField()
    noTarjeta = models.IntegerField()
    fechaAsignacion = models.DateField()

    class Meta:
        db_table = 'AsignacionTarjeta'

class Tarjeta(models.Model):
    noTarjeta = models.IntegerField()
    tipo = models.CharField(max_length=200)
    limite = models.FloatField()
    fechaCorte = models.DateField()
    fechaPago = models.DateField()

    class Meta:
        db_table = 'Tarjeta'

class Emisor(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        db_table = 'Emisor'

class InteresEmisor(models.Model):
    porcentaje = models.FloatField()
    descripcion = models.CharField(max_length=200)

    class Meta:
        db_table = 'InteresEmisor'

class AsignacionTasaEmisor(models.Model):
    idEmisor = models.IntegerField()
    idInteresEmisor = models.IntegerField()

    class Meta:
        db_table = 'AsignacionTasaEmisor'

class Afiliado(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    telefono = models.IntegerField()
    correo = models.EmailField()
    bloqueado = models.BooleanField(default=False)

    class Meta:
        db_table = 'Afiliado'

class TipoAfiliado(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    porcentaje = models.FloatField()
    bloqueado = models.BooleanField(default=False)

    class Meta:
        db_table = 'TipoAfiliado'
