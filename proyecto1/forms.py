__author__ = 'huamacar'

from django import forms

class UsuarioForm(forms.Form):
        nombre = forms.CharField(label='Nombre cliente', max_length=100)

class EditarUsuarioForm(forms.Form):
        nombreAnterior = forms.CharField(label='Nombre anterior', max_length=100)
        nombre = forms.CharField(label='Nombre nuevo', max_length=100, required=False)
        eliminar = forms.BooleanField(required=False)