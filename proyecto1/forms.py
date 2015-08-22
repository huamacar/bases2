__author__ = 'huamacar'

from django import forms
from django.forms import ModelForm
from proyecto1.models import *
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
class UsuarioForm(ModelForm):
        class Meta:
            model = Usuario
            fields = '__all__'
'''
class EditarUsuarioForm(ModelForm):
        nombreAnterior = forms.CharField(label='Nombre anterior', max_length=100)
        nombre = forms.CharField(label='Nombre nuevo', max_length=100, required=False)
        eliminar = forms.BooleanField(required=False)
'''
class BuscarCliente(forms.Form):
        id = forms.IntegerField(label="Cliente Buscado")

class CuentaForm(ModelForm):
        class Meta:
            model = Cuenta
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
