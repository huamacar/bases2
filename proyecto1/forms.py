__author__ = 'huamacar'

from django import forms
from django.forms import ModelForm
from proyecto1.models import *
from django.core.validators import *
'''
class UsuarioForm(forms.Form):
        nombre = forms.CharField(label='Nombre cliente', max_length=100)
        direccion = forms.CharField(label='Direccion', max_length=100)
        telefono = forms.IntegerField(label='Telefono')
        correo = forms.EmailField(label='Correo')
        fechaNacimiento = forms.DateField(label='Fecha Nacimiento')
        profesion = forms.CharField(label='Profesion', max_length=100)
        genero = forms.CharField(label='Genero', max_length=100)
'''
class ClienteForm(ModelForm):
        class Meta:
            model = Cliente
            fields = '__all__'

class TransaccionForm(ModelForm):
        class Meta:
            model = Transaccion
            fields = '__all__'
'''
class EditarUsuarioForm(ModelForm):
        nombreAnterior = forms.CharField(label='Nombre anterior', max_length=100)
        nombre = forms.CharField(label='Nombre nuevo', max_length=100, required=False)
        eliminar = forms.BooleanField(required=False)
'''
class BuscarCliente(forms.Form):
        nombre = forms.CharField(max_length=200)

class RetirarEfectivo(forms.Form):
        cantidad = forms.FloatField(validators=[MinValueValidator(0.0)])

class CuentaForm(ModelForm):
        class Meta:
            model = Cuenta
            fields = '__all__'

class TipoCuentaForm(ModelForm):
        class Meta:
            model = TipoCuenta
            fields = '__all__'

class AsigCuentaForm(ModelForm):
        class Meta:
            model = AsignacionCuenta
            fields = '__all__'

class TarjetaForm(ModelForm):
        class Meta:
            model = Tarjeta
            fields = '__all__'

class AsigTarjetaForm(ModelForm):
        class Meta:
            model = AsignacionTarjeta
            fields = '__all__'

class AfiliadoForm(ModelForm):
        class Meta:
            model = Afiliado
            fields = '__all__'

class BuscarAfiliado(forms.Form):
        id = forms.IntegerField(label="Afiliado Buscado")

class TipoAfiliadoForm(ModelForm):
        class Meta:
            model = TipoAfiliado
            fields = '__all__'

class Buscar_TipoAfiliado(forms.Form):
        id = forms.IntegerField(label="Cliente Buscado")

class UsuarioForm(ModelForm):
        class Meta:
            model = Usuario
            fields = '__all__'

class BuscarCuentaForm(forms.Form):
        idCuenta = forms.IntegerField(label="Numero de cuenta", validators=[MinValueValidator(0)])

class PagarCuentaForm(forms.Form):
        monto = forms.FloatField(label="Monto a pagar", validators=[MinValueValidator(0)])

class TransferenciaCuentasForm(forms.Form):
        cuentaorigen = forms.IntegerField(label="Cuenta Origen", validators=[MinValueValidator(0)])
        cuentadestino = forms.IntegerField(label="Cuenta Destino", validators=[MinValueValidator(0)])
        monto = forms.FloatField(label="Monto a pagar", validators=[MinValueValidator(0)])

class LoteForm(ModelForm):
        class Meta:
            model = Lote
            fields = '__all__'

class AsigLoteForm(ModelForm):
        class Meta:
            model = AsignacionLoteUsuario
            fields = '__all__'

class NotasForm(ModelForm):
        class Meta:
            model = Nota
            fields = '__all__'

class CrearEstadoTarjetaForm(ModelForm):
        class Meta:
            model = TipoEstado
            fields = '__all__'

class DeclaCambioForm(ModelForm):
        class Meta:
            model = DeclaracionCambio
            fields = '__all__'
