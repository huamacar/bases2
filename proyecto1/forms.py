__author__ = 'huamacar'

from django import forms

class UsuarioForm(forms.Form):
        nombre = forms.CharField(label='Nombre cliente', max_length=100)