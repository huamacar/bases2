from django.db import models
# Amadeus was here 2
# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    telefono = models.IntegerField()
    correo = models.EmailField()
    fechaNacimiento = models.DateField()
    profesion = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    bloqueado = models.BooleanField(default=False)

    class Meta:
        db_table = 'Cliente'

class TipoCuenta(models.Model):
    tipoCuenta = models.CharField(max_length=200)

    class Meta:
        db_table = 'TipoCuenta'

class Cuenta(models.Model):
    idTipoCuenta = models.ForeignKey(TipoCuenta)
    limite = models.FloatField()
    fechaCreacion = models.DateField()
    diasMorosos = models.IntegerField()

    class Meta:
        db_table = 'Cuenta'

class InteresCliente(models.Model):
    porcentaje = models.FloatField()
    descripcion = models.CharField(max_length=200)

    class Meta:
        db_table = 'InteresCliente'

class AsigancionTasaCliente(models.Model):
    idCuenta = models.ForeignKey(Cuenta)
    idTasaInteres = models.ForeignKey(InteresCliente)

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
    tipoTarjeta = models.CharField(max_length=200)

    class Meta:
        db_table = 'TipoTarjeta'

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
    idEmisor = models.ForeignKey(Emisor)
    idInteresEmisor = models.ForeignKey(InteresEmisor)

    class Meta:
        db_table = 'AsignacionTasaEmisor'

class Tarjeta(models.Model):
    noTarjeta = models.IntegerField()
    tipoTarjeta = models.ForeignKey(TipoTarjeta)
    idEmisor = models.ForeignKey(Emisor)
    idAsignacion = models.ForeignKey(AsignacionTasaEmisor)
    limite = models.FloatField()
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
        db_table = 'InteresEmisor'

class TipoEstado(models.Model):
    tipoEstado = models.CharField(max_length=100)
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
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    porcentaje = models.FloatField()

    class Meta:
        db_table = 'TipoAfiliado'

class Usuario(models.Model):
    idRol = models.ForeignKey(Rol)
    usuario = models.CharField(max_length=100)
    password = models.CharField(max_length=200)

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
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    telefono = models.IntegerField()
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

class Nota(models.Model):
    nota = models.CharField(max_length=100)
    fecha = models.DateField()
    descripcion = models.CharField(max_length=200)

    class Meta:
        db_table = 'Nota'

class TipoTransaccion(models.Model):
    tipoTransaccion = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)

    class Meta:
        db_table = 'TipoTransaccion'

class Transaccion(models.Model):
    idTipoTrasaccion = models.ForeignKey(TipoTransaccion)
    fecha = models.DateField()
    hora = models.DateTimeField()
    monto = models.FloatField()

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
    idNota = models.ForeignKey(Nota)
    idLote = models.ForeignKey(Lote)
    idTrasaccion = models.ForeignKey(Transaccion)
    fecha = models.DateField()

    class Meta:
        db_table = 'Recibo'

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