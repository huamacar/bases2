__author__ = 'huamacar'

from functools import partial
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

DateInput = partial(forms.DateInput, {'class': 'datepicker'})
class ClienteForm(ModelForm):
        def __init__(self, *args, **kwargs):
            super(ClienteForm, self).__init__(*args, **kwargs)
            self.fields['fechaNacimiento'].widget=DateInput()
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

class BuscarSenda(forms.Form):
        cuenta = forms.IntegerField()

class RetirarEfectivo(forms.Form):
        cantidad = forms.FloatField(validators=[MinValueValidator(0.0)])

class CuentaForm(ModelForm):
        def __init__(self, *args, **kwargs):
            super(CuentaForm, self).__init__(*args, **kwargs)
            self.fields['fechaCreacion'].widget=DateInput()
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
        def __init__(self, *args, **kwargs):
            super(TarjetaForm, self).__init__(*args, **kwargs)
            self.fields['fechaCorte'].widget=DateInput()
            self.fields['fechaPago'].widget=DateInput()
        class Meta:
            model = Tarjeta
            fields = '__all__'

class AsigTarjetaForm(ModelForm):
        def __init__(self, *args, **kwargs):
            super(AsigTarjetaForm, self).__init__(*args, **kwargs)
            self.fields['fechaAsignacion'].widget=DateInput()

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
        id = forms.IntegerField(label="Tipo de Afiliado")

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
        def __init__(self, *args, **kwargs):
           super(NotasForm, self).__init__(*args, **kwargs)
           self.fields['fecha'].widget=DateInput()
        class Meta:
            model = Nota
            fields = '__all__'

class CrearEstadoTarjetaForm(ModelForm):
        class Meta:
            model = TipoEstado
            fields = '__all__'

class DeclaCambioForm(ModelForm):
        def __init__(self, *args, **kwargs):
            super(DeclaCambioForm, self).__init__(*args, **kwargs)
            self.fields['fecha'].widget=DateInput()
        class Meta:
            model = DeclaracionCambio
            fields = '__all__'
