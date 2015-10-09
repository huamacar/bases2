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
        self.fields['fechaNacimiento'].widget = DateInput()

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
        nombre = forms.CharField(label='Nombre nue4', max_length=100, required=False)
        eliminar = forms.BooleanField(required=False)
'''


class BuscarCliente(forms.Form):
    nombre = forms.CharField(max_length=200)


class BuscarSenda(forms.Form):
    cuenta = forms.IntegerField()


class RetirarEfectivo(forms.Form):
    cantidad = forms.FloatField(validators=[MinValueValidator(0.0)])


class TarjetaListaNegra(forms.Form):
    razon = forms.CharField(max_length=200)


class CuentaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CuentaForm, self).__init__(*args, **kwargs)
        self.fields['fechaCreacion'].widget = DateInput()

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
        self.fields['fechaCorte'].widget = DateInput()
        self.fields['fechaPago'].widget = DateInput()

    class Meta:
        model = Tarjeta
        fields = '__all__'


class AsigTarjetaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AsigTarjetaForm, self).__init__(*args, **kwargs)
        self.fields['fechaAsignacion'].widget = DateInput()

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
    idAfi = forms.ModelChoiceField(label='Tipo de afiliado',
                                   queryset=TipoAfiliado.objects.all().values_list('nombre', flat=True))


class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'


class BuscarCuentaForm(forms.Form):
    idCuenta = forms.IntegerField(label="Numero de cuenta", validators=[MinValueValidator(0)])


class BuscarTarjetaForm(forms.Form):
    noTarjeta = forms.IntegerField(label="Numero de Tarjeta", validators=[MinValueValidator(1000000000000000),
                                                                          MaxValueValidator(9999999999999999)])


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


class AsigUsuarioLoteForm(ModelForm):
    class Meta:
        model = AsignacionLoteUsuario
        fields = '__all__'


class AsigAfiliadoLoteForm(ModelForm):
    class Meta:
        model = AsignacionLoteAfiliado
        fields = '__all__'


class NotasForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(NotasForm, self).__init__(*args, **kwargs)
        self.fields['fecha'].widget = DateInput()

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
        self.fields['fecha'].widget = DateInput()

    class Meta:
        model = DeclaracionCambio
        fields = '__all__'


class AsigInteresEmisorForm(ModelForm):
    class Meta:
        model = AsignacionTasaEmisor
        fields = '__all__'


class EmisorForm(ModelForm):
    class Meta:
        model = Emisor
        fields = '__all__'


class AsigInteresCuentaForm(ModelForm):
    class Meta:
        model = AsigancionTasaCliente
        fields = '__all__'


class RolForm(ModelForm):
    class Meta:
        model = Rol
        fields = '__all__'


class AutorizarRolForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AutorizarRolForm, self).__init__(*args, **kwargs)
        self.fields['fecha'].widget = DateInput()

    class Meta:
        model = Autorizacion
        fields = '__all__'


class PrivilegioRolForm(ModelForm):
    class Meta:
        model = Privilegio
        fields = '__all__'


class Buscar_RolForm(forms.Form):
    idRol = forms.ModelChoiceField(label='Rol', queryset=Rol.objects.all().values_list('rol', flat=True))


class TipoTarjetaForm(ModelForm):
    class Meta:
        model = TipoTarjeta
        fields = '__all__'


class VoucherForm(ModelForm):
    class Meta:
        model = Voucher
        fields = '__all__'

class ReciboForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReciboForm, self).__init__(*args, **kwargs)
        self.fields['fecha'].widget = DateInput()
    class Meta:
        model = Recibo
        fields = '__all__'

class Buscar_TTarjetaForm(forms.Form):
    idTT = forms.ModelChoiceField(label='Tipo Tarjeta',
                                  queryset=TipoTarjeta.objects.all().values_list('tipoTarjeta', flat=True))


class Buscar_EmisorForm(forms.Form):
    idEmisor = forms.ModelChoiceField(label='Emisor', queryset=Emisor.objects.all().values_list('nombre', flat=True))


class Buscar_PrivilegioForm(forms.Form):
    idPrivilegio = forms.ModelChoiceField(label='Privilegio',
                                          queryset=Privilegio.objects.all().values_list('privilegio', flat=True))


class Buscar_AutorizacionForm(forms.Form):
    idAutorizacion = forms.ModelChoiceField(label='Autorizacion',
                                            queryset=Autorizacion.objects.all().values_list('autorizacion', flat=True))


class Buscar_TipoEstadoForm(forms.Form):
    idTipoEstado = forms.ModelChoiceField(label='TipoEstado',
                                          queryset=TipoEstado.objects.all().values_list('tipoEstado', flat=True))


class Buscar_TipoCuentaForm(forms.Form):
    idTipoCuenta = forms.ModelChoiceField(label='TipoCuenta',
                                          queryset=TipoCuenta.objects.all().values_list('tipoCuenta', flat=True))

class UploadFileForm(forms.Form):
    file = forms.FileField()