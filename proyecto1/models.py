from django.db import models
from django.core.validators import *
from django import forms
# Amadeus was here 2
# Create your models here.

GENERO_CHOICES = (
    ('masculino', 'masculino'),
    ('femenino', 'femenino'),
)


INTERES_CHOICES = (
    (0.5,'5%'),
    (0.1,'10%'),
    (0.15,'15%'),
    (0.2,'20%'),
    (0.25,'25%'),
    (0.3,'30%'),
    (0.35,'35%'),
    (0.4,'40%'),
    (0.45,'45%'),
    (0.5,'50%'),
    (0.55,'55%'),
    (0.6,'60%'),
    (0.65,'65%'),
    (0.7,'70%'),
    (0.75,'75%'),
)

PROGRAMA_CHOICES = (
    ('deposito','deposito'),
    ('pago cheque', 'pago cheque'),
    ('retiro','retiro'),
)

class Cliente(models.Model):
    nombre = models.CharField(max_length=200, validators=[RegexValidator(r'^[a-zA-Z\' \']*$', 'El nombre solo permite letras de A-Z')])
    direccion = models.CharField(max_length=200, validators=[RegexValidator(r'^[0-9a-zA-Z\'\-\'\' \']*$', 'La dirreccion no permite simbolos extranios')])
    telefono = models.IntegerField(validators=[MaxValueValidator(99999999),MinValueValidator(10000000)])
    correo = models.EmailField()
    fechaNacimiento = models.DateField()
    profesion = models.CharField(max_length=200, validators=[RegexValidator(r'^[0-9a-zA-Z\'\-\'\' \']*$', 'La profesion no permite simbolos extranios')])
    genero = models.CharField(max_length=50, choices=GENERO_CHOICES)
    bloqueado = models.BooleanField(default=False)

    class Meta:
        db_table = 'Cliente'

class TipoCuenta(models.Model):
    tipoCuenta = models.CharField(max_length=200, validators=[RegexValidator(r'^[0-9a-zA-Z\'\-\'\' \']*$', 'El tipo de cuenta no permite simbolos extranios')])

    class Meta:
        db_table = 'TipoCuenta'

class Cuenta(models.Model):
    idTipoCuenta = models.ForeignKey(TipoCuenta)
    limite = models.FloatField(validators=[MinValueValidator(0.0)])
    fechaCreacion = models.DateField()
    diasMorosos = models.IntegerField(validators=[MinValueValidator(0)])
    saldo = models.FloatField(validators=[MinValueValidator(0.0)])

    class Meta:
        db_table = 'Cuenta'


class AsigancionTasaCliente(models.Model):
    idCuenta = models.ForeignKey(Cuenta)
    idTasaInteres = models.FloatField(choices=INTERES_CHOICES)

    class Meta:
        db_table = 'AsigancionTasaCliente'

class AsignacionCuenta(models.Model):
    idCliente = models.ForeignKey(Cliente)
    idCuenta = models.ForeignKey(Cuenta)

    class Meta:
        db_table = 'AsignacionCuenta'

class AsignacionTarjeta(models.Model):
    idCuenta = models.ForeignKey(Cuenta)
    noTarjeta = models.IntegerField()
    fechaAsignacion = models.DateField()

    class Meta:
        db_table = 'AsignacionTarjeta'

class TipoTarjeta(models.Model):
    tipoTarjeta = models.CharField(max_length=200, validators=[RegexValidator(r'^[0-9a-zA-Z\'\-\'\' \']*$', 'El tipo de tarjeta no permite simbolos extranios')])

    class Meta:
        db_table = 'TipoTarjeta'

class Emisor(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        db_table = 'Emisor'

class AsignacionTasaEmisor(models.Model):
    idEmisor = models.ForeignKey(Emisor)
    idInteresEmisor = models.FloatField(choices=INTERES_CHOICES)

    class Meta:
        db_table = 'AsignacionTasaEmisor'

class Tarjeta(models.Model):
    noTarjeta = models.IntegerField(validators=[MaxValueValidator(1000000000000000),MinValueValidator(9999999999999999)])
    tipoTarjeta = models.ForeignKey(TipoTarjeta)
    idEmisor = models.ForeignKey(Emisor)
    idAsignacion = models.ForeignKey(AsignacionTasaEmisor)
    limite = models.FloatField(validators=[MinValueValidator(0.0)])
    fechaCorte = models.DateField()
    fechaPago = models.DateField()

    class Meta:
        db_table = 'Tarjeta'

class PagoMinimo(models.Model):
    idTarjeta = models.ForeignKey(Tarjeta)
    mes = models.IntegerField(max_length=2)
    anio = models.IntegerField(max_length=4)
    monto = models.FloatField()

    class Meta:
        db_table = 'PagoMinimo'

class TipoEstado(models.Model):
    tipoEstado = models.CharField(max_length=100, validators=[RegexValidator(r'^[0-9a-zA-Z\'\-\'\' \']*$', 'El tipo de estado no permite simbolos extranios')])
    descripcion = models.CharField(max_length=200)

    class Meta:
        db_table = 'TipoEstado'

class DeclaracionCambio(models.Model):
    idTarjeta = models.ForeignKey(Tarjeta)
    idEstado = models.ForeignKey(TipoEstado)
    fecha = models.DateField()

    class Meta:
        db_table = 'DeclaracionCambio'

class Rol(models.Model):
    rol = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)

    class Meta:
        db_table = 'Rol'

class Autorizacion(models.Model):
    idRol = models.ForeignKey(Rol)
    autorizacion = models.CharField(max_length=100)
    fecha = models.DateField()
    descripcion = models.CharField(max_length=200)

    class Meta:
        db_table = 'Autorizacion'

class Privilegio(models.Model):
    idRol = models.ForeignKey(Rol)
    privilegio = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)

    class Meta:
        db_table = 'Privilegio'

class TipoAfiliado(models.Model):
    nombre = models.CharField(max_length=200, validators=[RegexValidator(r'^[0-9a-zA-Z\'\-\'\' \']*$', 'El tipo de afiliado no permite simbolos extranios')])
    descripcion = models.CharField(max_length=200)
    porcentaje = models.FloatField(choices=INTERES_CHOICES)

    class Meta:
        db_table = 'TipoAfiliado'

class Usuario(models.Model):
    idRol = models.ForeignKey(Rol)
    usuario = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    correo = models.EmailField(max_length= 200)

    class Meta:
        db_table = 'Usuario'

class ListaAcceso(models.Model):
    idUsuario = models.ForeignKey(Usuario)
    fecha = models.DateField()
    hora = models.DateTimeField()
    descripcion = models.CharField(max_length=200)

    class Meta:
        db_table = 'ListaAcceso'

class Lote(models.Model):
    lote = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)

    class Meta:
        db_table = 'Lote'

class Afiliado(models.Model):
    nombre = models.CharField(max_length=200, validators=[RegexValidator(r'^[a-zA-Z\' \']*$', 'El nombre solo permite letras de A-Z')])
    direccion = models.CharField(max_length=200, validators=[RegexValidator(r'^[0-9a-zA-Z\'\-\'\' \']*$', 'La dirreccion no permite simbolos extranios')])
    telefono = models.IntegerField(validators=[MaxValueValidator(99999999),MinValueValidator(10000000)])
    correo = models.EmailField()
    tipoAfiliado = models.ForeignKey(TipoAfiliado)
    bloqueado = models.BooleanField(default=False)

    class Meta:
        db_table = 'Afiliado'

class AsignacionLoteAfiliado(models.Model):
    idAfiliado = models.ForeignKey(Afiliado)
    idLote = models.ForeignKey(Lote)

    class Meta:
        db_table = 'AsignacionLoteAfiliado'

class AsignacionLoteUsuario(models.Model):
    idUsuario = models.ForeignKey(Usuario)
    idLote = models.ForeignKey(Lote)

    class Meta:
        db_table = 'AsignacionLoteUsuario'

NOTASTIPO_CHOICES = (
    ('debito', 'debito'),
    ('credito', 'credito'),
)

class Transaccion(models.Model):
    tipoTrasaccion = models.CharField(max_length=100, choices=NOTASTIPO_CHOICES)
    fecha = models.DateField()
    hora = models.DateTimeField()
    monto = models.FloatField()
    autorizacion = models.BooleanField(default=False)

    class Meta:
        db_table = 'Transaccion'

class Voucher(models.Model):
    idLote = models.ForeignKey(Lote)
    idTrasaccion = models.ForeignKey(Transaccion)
    monto = models.FloatField()
    descripcion = models.CharField(max_length=200)

    class Meta:
        db_table = 'Voucher'

class Recibo(models.Model):
    idUsuario = models.ForeignKey(Usuario)
    idLote = models.ForeignKey(Lote)
    idTrasaccion = models.ForeignKey(Transaccion)
    fecha = models.DateField()

    class Meta:
        db_table = 'Recibo'

class Nota(models.Model):
    idRecibo = models.ForeignKey(Recibo)
    nota = models.CharField(max_length=100, choices=NOTASTIPO_CHOICES)
    fecha = models.DateField()
    descripcion = models.CharField(max_length=200)

    class Meta:
        db_table = 'Nota'

class Programa(models.Model):
    programa = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)

    class Meta:
        db_table = 'Programa'

class Log(models.Model):
    idUsuario = models.ForeignKey(Usuario)
    idTrasaccion = models.ForeignKey(Transaccion)
    idCuenta = models.ForeignKey(Cuenta)
    idPrograma = models.ForeignKey(Programa)
    fecha = models.DateField()
    hora = models.DateTimeField()
    saldo_inicial = models.FloatField()
    saldo = models.FloatField()
    debito = models.FloatField()
    credito = models.FloatField()
    autorizacion = models.BooleanField(default=False)
    rechazo = models.BooleanField(default=False)
    razonRechazo = models.CharField(max_length=200)

    class Meta:
        db_table = 'Log'