__author__ = 'huamacar'

from django import forms

class UsuarioForm(forms.Form):
        nombre = forms.CharField(label='Nombre cliente', max_length=100)
        direccion = forms.CharField(label='Direccion', max_length=100)
        telefono = forms.IntegerField(label='Telefono')
        correo = forms.EmailField(label='Correo')
        fechaNacimiento = forms.DateField(label='Fecha Nacimiento')
        profesion = forms.CharField(label='Profesion', max_length=100)
        genero = forms.CharField(label='Genero', max_length=100)

class EditarUsuarioForm(forms.Form):
        nombreAnterior = forms.CharField(label='Nombre anterior', max_length=100)
        nombre = forms.CharField(label='Nombre nuevo', max_length=100, required=False)
        eliminar = forms.BooleanField(required=False)

class BuscarCliente(forms.Form):
        id = forms.IntegerField(label="Cliente Buscado")

class CuentaForm(forms.Form):
        tipo = forms.CharField(label='Tipo de Cuenta', max_length=100)
        limite = forms.FloatField(label='Limite')
        fechaCreacion = forms.DateField(label='Fecha de Creacion')

class AsigCuentaForm(forms.Form):
        idUsuario = forms.IntegerField(label='Id Usuario')
        idCuenta = forms.IntegerField(label='Id Cuenta')

class TarjetaForm(forms.Form):
        noTarjeta = forms.IntegerField(label='No Tarjeta')
        tipo = forms.CharField(label='Tipo de Tarjeta', max_length=100)
        limite = forms.FloatField(label='Limite')
        fechaCorte = forms.DateField(label='Fecha de Corte')
        fechaPago = forms.DateField(label='Fecha de Pago')

class AsigTarjetaForm(forms.Form):
        idCuenta = forms.IntegerField(label='Id Cuenta')
        noTarjeta = forms.IntegerField(label='No Tarjeta')
        fechaAsignacion = forms.DateField(label='Fecha de Asignacion')