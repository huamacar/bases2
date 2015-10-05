import datetime

from django.shortcuts import render, render_to_response
# Create your views here.

from .forms import *
from django.http import HttpResponse
from django.db.models import Q
from django.contrib import messages  # para emitir aletrs
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def index(request):
    return render(request, 'Index.html')


@login_required(login_url='/login')
def indexClientes(request):
    messages.add_message(request, messages.INFO, 'Area de operacion de clientes.')
    return render(request, 'Clientes/Index.html')


@login_required(login_url='/login')
def indexAutorizacion(request):
    messages.add_message(request, messages.INFO, 'Area de operacion de Autorizaciones.')
    return render(request, 'Autorizacion/Index.html')

@login_required(login_url='/login')
def indexSenda(request):
    messages.add_message(request, messages.INFO, 'Ver Senda.')
    return render(request, 'Senda/Index.html')

@login_required(login_url='/login')
def indexListaNegra(request):
    messages.add_message(request, messages.INFO, 'Ver Lista Negra.')
    return render(request, 'ListaNegra/Index.html')

@login_required(login_url='/login')
def indexCuentas(request):
    return render(request, 'Cuentas/Index.html')

@login_required(login_url='/login')
def indexCaja(request):
    return render(request, 'Caja/Index.html')


@login_required(login_url='/login')
def indexTarjetas(request):
    return render(request, 'Tarjetas/Index.html')


@login_required(login_url='/login')
def indexAfiliado(request):
    return render(request, 'Afiliado/Index.html')


@login_required(login_url='/login')
def indexTipoAfiliado(request):
    return render(request, 'TipoAfiliado/Index.html')

@login_required(login_url='/login')
def indexLotes(request):
    return render(request, 'Lote/Index.html')

@login_required(login_url='/login')
def indexNotas(request):
    return render(request, 'Notas/Index.html')

@login_required(login_url='/login')
def indexEmisor(request):
    return render(request, 'Emisor/Index.html')

@login_required(login_url='/login')
def indexRol(request):
    return render(request, 'Rol/Index.html')

@login_required(login_url='/login')
def indexTipoTarjeta(request):
    return render(request, 'TipoTarjeta/Index.html')

@login_required(login_url='/login')
def insertarClientes(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)

        if form.is_valid():
            form.save()  # con esto no hay necesidad de igualar los datos ya se salva a la base de datos
            form = ClienteForm()
            messages.add_message(request, messages.INFO, 'El Cliente se ha insertado')
            return render(request, 'Clientes/Insertar.html', {'form': form})
    else:
        form = ClienteForm()

    return render(request, 'Clientes/Insertar.html', {'form': form})


@login_required(login_url='/login')
def Bloquear_Clientes(request, id):
    u = Usuario.objects.get(id=id)
    u.bloqueado = True
    u.save()
    messages.add_message(request, messages.INFO, 'El usuario ha sido bloqueado')
    form = BuscarCliente()
    return render(request, 'Clientes/Buscar.html', {'form': form})


@login_required(login_url='/login')
def Lista_Clientes(request):
    usuarios = Usuario.objects.all()
    return render(request, 'Clientes/ListaUsuarios.html', {'usuarios': usuarios})


@login_required(login_url='/login')
def Buscar_Clientes(request):
    if request.method == 'POST':
        form = BuscarCliente(request.POST)
        if form.is_valid():
            nombrecliente = form.cleaned_data['nombre']
            try:
                clientes = Cliente.objects.filter(Q(
                    nombre__startswith=nombrecliente)).values()

                return render(request, 'Clientes/ListaUsuarios.html', {'clientes': clientes})
            except:
                return render(request, 'Clientes/ListaUsuarios.html')

    else:
        form = BuscarCliente()

    return render(request, 'Clientes/Buscar.html', {'form': form})

@login_required(login_url='/login')
def BuscarClienteAjax(request):
    if request.method == 'POST':
        search_text = request.POST['search_text']
    else:
        search_text = 0

    clientes = Cliente.objects.filter(nombre__istartswith=search_text)

    return render(request, 'Clientes/busqueda_ajax.html', {'clientes': clientes})



@login_required(login_url='/login')
def consumo(request):
    transacciones = Transaccion.objects.all()

    return render(request, 'Autorizacion/Consumo.html', {'transacciones': transacciones})

@login_required(login_url='/login')
def listanegra(request):
    listanegra = ListaNegra.objects.all()

    return render(request, 'ListaNegra/ListaNegra.html', {'listanegra': listanegra})

@login_required(login_url='/login')
def senda(request):
    logs = Log.objects.all()

    return render(request, 'Senda/Senda.html', {'logs': logs})

@login_required(login_url='/login')
def buscarSenda(request):
    if request.method == 'POST':
        form = BuscarSenda(request.POST)
        if form.is_valid():
            noCuenta = form.data['cuenta']
            try:
                logs = Log.objects.filter(Q(
                    idCuenta__gte=noCuenta)).all()

                return render(request, 'Senda/Senda.html', {'logs': logs})
            except:
                return render(request, 'Senda/Senda.html')

    else:
        form = BuscarSenda()
        return render(request, 'Senda/Buscar.html', {'form': form})

@login_required(login_url='/login')
def autorizar(request, id):
    if request.method == 'POST':

        u = Transaccion.objects.get(id=id)
        form = TransaccionForm(request.POST, instance=u)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'La transaccion ha sido autorizada')
            idusuario = u.id
            return render(request, 'Autorizacion/Autorizar.html', {'form': form, 'idusuario': idusuario})
    else:
        u = Transaccion()
        try:
            u = Transaccion.objects.get(id=id)
        except:
            messages.add_message(request, messages.INFO, 'El usuario no existe en la base de datos')
            form = TransaccionForm(instance=u)
            idusuario = u.id
            return render(request, 'Autorizacion/Autorizar.html', {'form': form, 'idusuario': idusuario})
        form = TransaccionForm(instance=u)

    idusuario = u.id
    return render(request, 'Autorizacion/Autorizar.html', {'form': form, 'idusuario': idusuario})


@login_required(login_url='/login')
def Eliminar_Clientes(request, id):
    Usuario.objects.get(id=id).delete()
    messages.add_message(request, messages.INFO, 'El usuario ha sido eliminado')
    form = BuscarCliente()
    return render(request, 'Clientes/Buscar.html', {'form': form})


@login_required(login_url='/login')
def crearCuenta(request):
    if request.method == 'POST':
        form = CuentaForm(request.POST)
        idform = form.data['idTipoCuenta']
        form.data = form.data.copy()
        form.data['idTipoCuenta'] = TipoCuenta.objects.filter(tipoCuenta=idform).values_list('id', flat=True)
        if form.is_valid():
            form.save()
            form = CuentaForm()
            messages.add_message(request, messages.INFO, 'La cuenta se ha creado')
            return render(request, 'Cuentas/Crear.html', {'form': form})
    else:
        form = CuentaForm()
        form.fields["idTipoCuenta"].queryset = TipoCuenta.objects.all().values_list('tipoCuenta',flat=True)
    return render(request, 'Cuentas/Crear.html', {'form': form})


@login_required(login_url='/login')
def crearTipoCuenta(request):
    if request.method == 'POST':
        form = TipoCuentaForm(request.POST)

        if form.is_valid():
            form.save()
            form = TipoCuentaForm()
            messages.add_message(request, messages.INFO, 'El tipo de cuenta ha sido creada')
            return render(request, 'Cuentas/CrearTipo.html', {'form': form})
    else:
        form = TipoCuentaForm()

    return render(request, 'Cuentas/CrearTipo.html', {'form': form})


@login_required(login_url='/login')
def asignarCuenta(request):
    if request.method == 'POST':
        form = AsigCuentaForm(request.POST)

        idform = form.data['idCliente']
        form.data = form.data.copy()
        form.data['idCliente'] = Cliente.objects.filter(nombre=idform).values_list('id', flat=True)

        if form.is_valid():
            form.save()
            form = AsigCuentaForm()
            messages.add_message(request, messages.INFO, 'La cuenta ha sido asignada')
            form.fields["idCliente"].queryset = Cliente.objects.all().values_list('nombre',flat=True)  # se llena el form con los valores
            form.fields["idCuenta"].queryset = Cuenta.objects.all().values_list('id',flat=True)  # se llena el form con los valores
            return render(request, 'Cuentas/AsignarCuenta.html', {'form': form})
    else:
        form = AsigCuentaForm()
    form.fields["idCliente"].queryset = Cliente.objects.all().values_list('nombre',flat=True)  # se llena el form con los valores
    form.fields["idCuenta"].queryset = Cuenta.objects.all().values_list('id',flat=True)  # se llena el form con los valores
    return render(request, 'Cuentas/AsignarCuenta.html', {'form': form})


@login_required(login_url='/login')
def crearTarjeta(request):
    if request.method == 'POST':
        form = TarjetaForm(request.POST)

        idform = form.data['idEmisor']
        form.data = form.data.copy()
        form.data['idEmisor'] = Emisor.objects.filter(nombre=idform).values_list('id', flat=True)

        idtform = form.data['tipoTarjeta']
        form.data = form.data.copy()
        form.data['tipoTarjeta'] = TipoTarjeta.objects.filter(tipoTarjeta=idtform).values_list('id', flat=True)

        if form.is_valid():
            form.save()
            form = TarjetaForm()
            messages.add_message(request, messages.INFO, 'La tarjeta ha sido creada')
            form.fields["idEmisor"].queryset = Emisor.objects.all().values_list('nombre',flat=True)  # se llena el form con los valores
            form.fields["tipoTarjeta"].queryset = TipoTarjeta.objects.all().values_list('tipoTarjeta',flat=True)  # se llena el form con los valores
            return render(request, 'Tarjetas/CrearTarjeta.html', {'form': form})
    else:
        form = TarjetaForm()
    form.fields["idEmisor"].queryset = Emisor.objects.all().values_list('nombre',flat=True)  # se llena el form con los valores
    form.fields["tipoTarjeta"].queryset = TipoTarjeta.objects.all().values_list('tipoTarjeta',flat=True)  # se llena el form con los valores
    return render(request, 'Tarjetas/CrearTarjeta.html', {'form': form})


@login_required(login_url='/login')
def asignarTarjeta(request):
    if request.method == 'POST':
        form = AsigTarjetaForm(request.POST)

        if form.is_valid():
            form.save()
            form = AsigTarjetaForm()
            form.fields["idCuenta"].queryset = Cuenta.objects.all().values_list('id',flat=True)  # se llena el form con los valores
            messages.add_message(request, messages.INFO, 'La tarjeta ha sido asignada')
            return render(request, 'Tarjetas/AsignarTarjeta.html', {'form': form})
    else:
        form = AsigTarjetaForm()
    form.fields["idCuenta"].queryset = Cuenta.objects.all().values_list('id',flat=True)  # se llena el form con los valores
    return render(request, 'Tarjetas/AsignarTarjeta.html', {'form': form})


@login_required(login_url='/login')
def editarClientes(request, id):
    if request.method == 'POST':
        u = Cliente.objects.get(id=id)
        form = ClienteForm(request.POST, instance=u)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'El usuario ha sido editado')
            idusuario = u.id
            return render(request, 'Clientes/Editar.html', {'form': form, 'idusuario': idusuario})
    else:
        u = Cliente()
        try:
            u = Cliente.objects.get(id=id)
        except:
            messages.add_message(request, messages.INFO, 'El usuario no existe en la base de datos')
            form = ClienteForm(instance=u)
            idusuario = u.id
            return render(request, 'Clientes/Editar.html', {'form': form, 'idusuario': idusuario})
        form = ClienteForm(instance=u)

    idusuario = u.id
    return render(request, 'Clientes/Editar.html', {'form': form, 'idusuario': idusuario})


@login_required(login_url='/login')
def insertarAfiliado(request):
    if request.method == 'POST':
        form = AfiliadoForm(request.POST)

        idform = form.data['tipoAfiliado']
        form.data = form.data.copy()
        form.data['tipoAfiliado'] = TipoAfiliado.objects.filter(nombre=idform).values_list('id', flat=True)
        if form.is_valid():
            form.save()
            form = AfiliadoForm()
            form.fields["tipoAfiliado"].queryset = TipoAfiliado.objects.all().values_list('nombre',flat=True)  # se llena el form con los valores
            messages.add_message(request, messages.INFO, 'El afiliado ha sido insertado')
            return render(request, 'Afiliado/Insertar.html', {'form': form})
    else:
        form = AfiliadoForm()
        form.fields["tipoAfiliado"].queryset = TipoAfiliado.objects.all().values_list('nombre',flat=True)  # se llena el form con los valores
    return render(request, 'Afiliado/Insertar.html', {'form': form})


@login_required(login_url='/login')
def Buscar_Afiliados(request):
    form = BuscarAfiliado(request.POST)
    u = None

    if form.is_valid():
        try:
            u = Afiliado.objects.get(id=form.cleaned_data['id'])
        except:
            messages.add_message(request, messages.INFO, 'El afiliado no existe en la base de datos')
            afiliado = BuscarAfiliado()
            return render(request, 'Afiliado/Buscar.html', {'form': afiliado, 'afiliado': u})

    afiliado = BuscarAfiliado()
    return render(request, 'Afiliado/Buscar.html', {'form': afiliado, 'afiliado': u})

@login_required(login_url='/login')
def BuscarAfiliadoAjax(request):
    if request.method == 'POST':
        search_text = request.POST['search_text']
    else:
        search_text = 0

    afiliados = Afiliado.objects.filter(nombre__istartswith=search_text)

    return render(request, 'Afiliado/busqueda_ajax.html', {'afiliados': afiliados})

@login_required(login_url='/login')
def Bloquear_Afiliados(request, id):
    u = Afiliado.objects.get(id=id)
    u.bloqueado = True
    u.save()
    messages.add_message(request, messages.INFO, 'El afiliado ha sido bloqueado')
    form = BuscarAfiliado()
    return render(request, 'Afiliado/Editar.html', {'form': form, 'idafiliado': u})

@login_required(login_url='/login')
def Eliminar_Afiliados(request, id):
    Afiliado.objects.get(id=id).delete()
    messages.add_message(request, messages.INFO, 'El afiliado ha sido eliminado')
    form = BuscarAfiliado()
    return render(request, 'Afiliado/Editar.html', {'form': form})


@login_required(login_url='/login')
def Eliminar_TipoAfiliados(request, id):
    TipoAfiliado.objects.get(id=id).delete()
    messages.add_message(request, messages.INFO, 'El tipo de afiliado ha sido eliminado')
    form = Buscar_TipoAfiliado()
    return render(request, 'TipoAfiliado/Buscar.html', {'form': form})


@login_required(login_url='/login')
def editarAfiliados(request, id):
    if request.method == 'POST':
        u = Afiliado.objects.get(id=id)
        form = AfiliadoForm(request.POST, instance=u)
        idform = form.data['tipoAfiliado']
        form.data = form.data.copy()
        form.data['tipoAfiliado'] = TipoAfiliado.objects.filter(nombre=idform).values_list('id', flat=True)
        if form.is_valid():
            form.save()
            form = BuscarAfiliado()
            messages.add_message(request, messages.INFO, 'El afiliado ha sido editado')
            return render(request, 'Afiliado/Buscar.html', {'form': form})
    else:
        form = Afiliado()
        try:
            u = Afiliado.objects.get(id=id)
        except:
            messages.add_message(request, messages.INFO, 'El afiliado no existe en la base de datos')
            form.fields["tipoAfiliado"].queryset = TipoAfiliado.objects.all().values_list('nombre',flat=True)  # se llena el form con los valores
            return render(request, 'Afiliado/Editar.html', {'form': form, 'idafiliado': u})
        form = AfiliadoForm(instance=u)

    idafiliado = u.id
    form.fields["tipoAfiliado"].queryset = TipoAfiliado.objects.all().values_list('nombre',flat=True)  # se llena el form con los valores
    return render(request, 'Afiliado/Editar.html', {'form': form, 'idafiliado': idafiliado})


@login_required(login_url='/login')
def insertarTipoAfiliado(request):
    if request.method == 'POST':
        form = TipoAfiliadoForm(request.POST)

        if form.is_valid():
            form.save()
            form = TipoAfiliadoForm()
            messages.add_message(request, messages.INFO, 'El tipo de afiliado se ha insertado')
            return render(request, 'TipoAfiliado/Insertar.html', {'form': form})
    else:
        form = TipoAfiliadoForm()

    return render(request, 'TipoAfiliado/Insertar.html', {'form': form})


@login_required(login_url='/login')
def BuscarTipoAfiliado(request):
     u = None
     if request.method == 'POST':
        form = Buscar_TipoAfiliado(request.POST)
        idform = form.data['idAfi']
        form.data = form.data.copy()
        form.data['idAfi'] = TipoAfiliado.objects.filter(nombre=idform).values_list('id', flat=True)
        if form.is_valid():
            idr = form.data['idAfi']
            u = TipoAfiliado.objects.get(id=idr)
            form = Buscar_TipoAfiliado()
            return render(request, 'TipoAfiliado/Buscar.html', {'form': form, 'TipoAfiliado': u})
     else:
        form = Buscar_TipoAfiliado()
     return render(request, 'TipoAfiliado/Buscar.html', {'form': form, 'TipoAfiliado': u})

@login_required(login_url='/login')
def editarTipoAfiliados(request, id):
    if request.method == 'POST':
        u = TipoAfiliado.objects.get(id=id)
        form = TipoAfiliadoForm(request.POST, instance=u)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'El tipo afiliado ha sido editado')
            form = Buscar_TipoAfiliado()
            return render(request, 'TipoAfiliado/Buscar.html', {'form': form, 'idTipoafiliado': u})
    else:
        form = TipoAfiliadoForm()
        try:
            u = TipoAfiliado.objects.get(id=id)
        except:
            messages.add_message(request, messages.INFO, 'EL tipo afiliado no existe en la base de datos')
            return render(request, 'TipoAfiliado/Editar.html', {'form': form, 'idTipoafiliado': u})
        form = TipoAfiliadoForm(instance=u)

    idTipoafiliado = u.id
    return render(request, 'TipoAfiliado/Editar.html', {'form': form, 'idTipoafiliado': idTipoafiliado})


@login_required(login_url='/login')
def RegistrarUsuario(request):
    if request.method == 'POST':

        form = UsuarioForm(request.POST)

        # se coloca el valor valido en el form, es decir el id en vez del nombre
        idform = form.data['idRol']
        form.data = form.data.copy()
        form.data['idRol'] = Rol.objects.filter(rol=idform).values_list('id', flat=True)

        if form.is_valid():
            User.objects.create_user(form.data['usuario'], form.data['correo'],
                                     form.data['password'])  # se guarda en la tabla de django
            form.save()
            form = UsuarioForm()
            messages.add_message(request, messages.INFO, 'The user has been created')
            return render(request, 'Usuarios/Registrar.html', {'form': form})
        form.fields["idRol"].queryset = Rol.objects.all().values_list('rol',
                                                                      flat=True)  # se llena el form con los valores de nuevo si hay error
    else:
        form = UsuarioForm()
        form.fields["idRol"].queryset = Rol.objects.all().values_list('rol',
                                                                      flat=True)  # se llena el form con los valores
    return render(request, 'Usuarios/Registrar.html', {'form': form})


@login_required(login_url='/login')
def BuscarCuenta(request):
    if request.method == 'POST':
        form = BuscarCuentaForm(request.POST)
        if form.is_valid():
            return render(request, 'Caja/Buscar.html', {'form': form})
    else:
        form = BuscarCuentaForm()

    return render(request, 'Caja/Buscar.html', {'form': form})

@login_required(login_url='/login')
def BuscarCuentaAjax(request):
    if request.method == 'POST':
        search_text = int(request.POST['search_text'])
    else:
        search_text = 0

    cuentas = Cuenta.objects.filter(id__startswith=search_text)
    # cuentas = Caja.objects.all().values()

    return render(request, 'Caja/busqueda_ajax.html', {'cuentas': cuentas})


@login_required(login_url='/login')
def PagarCuenta(request, id):
    if request.method == 'POST':
        c = Cuenta.objects.get(id=id)
        saldoInicial = c.saldo
        form = PagarCuentaForm(request.POST)
        if form.is_valid():
            monto = float(form.data['monto'])
            if monto > c.saldo:
                messages.add_message(request, messages.INFO, 'El monto no puede ser mayor al saldo')

                t = Transaccion()
                t.tipoTrasaccion = 'debito'
                t.fecha = datetime.datetime.now()
                t.hora = datetime.datetime.now()
                t.monto = monto
                t.save()

                l = Log()

                u = Usuario.objects.get(usuario=request.user.get_username())

                l.idTrasaccion = t
                l.idCuenta = c
                l.idPrograma = ""
                l.idUsuario = u
                l.fecha = datetime.datetime.now()
                l.hora = datetime.datetime.now()
                l.saldo_inicial = c.saldo
                l.saldo = c.saldo
                l.debito = monto
                l.credito = 0
                l.autorizacion = 0
                l.rechazo = 1
                l.razonRechazo = 'El monto no puede ser mayor al saldo'
                l.save()
            else:
                c.saldo = c.saldo - monto
                c.save()

                t = Transaccion()
                t.tipoTrasaccion = 'debito'
                t.fecha = datetime.datetime.now()
                t.hora = datetime.datetime.now()
                t.monto = monto
                t.save()

                l = Log()

                u = Usuario.objects.get(usuario=request.user.get_username())

                l.idTrasaccion = t
                l.idCuenta = c
                l.idPrograma = ""
                l.idUsuario = u
                l.fecha = datetime.datetime.now()
                l.hora = datetime.datetime.now()
                l.saldo_inicial = saldoInicial
                l.saldo = c.saldo
                l.debito = monto
                l.credito = 0
                l.autorizacion = 1
                l.rechazo = 0
                l.razonRechazo = ''
                l.save()

                messages.add_message(request, messages.INFO, 'El pago ha sido realizado')
                form = PagarCuentaForm()

            return render(request, 'Caja/pago.html', {'form': form, 'cuenta': c})
    else:
        c = Cuenta()
        c = Cuenta.objects.get(id=id)

        form = PagarCuentaForm()
    return render(request, 'Caja/pago.html', {'form': form, 'cuenta': c})


@login_required(login_url='/login')
def TransferenciaCuentas(request):
    t = False
    if request.method == 'POST':
        form = TransferenciaCuentasForm(request.POST)
        if form.is_valid():
            monto = float(form.data['monto'])
            errores = False
            cOrigen = Cuenta()
            cDestino= Cuenta()
            try:
                cOrigen = Cuenta.objects.get(id=form.data['cuentaorigen'])
            except:
                messages.add_message(request, messages.INFO, 'La cuenta origen no existe')
                errores = True

            try:
                cDestino = Cuenta.objects.get(id=form.data['cuentadestino'])
            except:
                messages.add_message(request, messages.INFO, 'La cuenta destino no existe')
                errores = True

            if not errores:
                if cOrigen.saldo >= monto:
                    saldoInicial = cDestino.saldo

                    cOrigen.saldo = cOrigen.saldo - monto
                    cDestino.saldo = cDestino.saldo + monto

                    cOrigen.save()
                    cDestino.save()

                    t = Transaccion()
                    t.tipoTrasaccion = 'debito'
                    t.fecha = datetime.datetime.now()
                    t.hora = datetime.datetime.now()
                    t.monto = monto
                    t.save()

                    l = Log()

                    u = Usuario.objects.get(usuario=request.user.get_username())

                    l.idTrasaccion = t
                    l.idCuenta = cDestino
                    l.idPrograma = ""
                    l.idUsuario = u
                    l.fecha = datetime.datetime.now()
                    l.hora = datetime.datetime.now()
                    l.saldo_inicial = saldoInicial
                    l.saldo = cDestino.saldo
                    l.debito = monto
                    l.credito = 0
                    l.autorizacion = 1
                    l.rechazo = 0
                    l.razonRechazo = ''
                    l.save()

                    messages.add_message(request, messages.INFO, 'Transaccion realizada con exito')
                    t = True;
                else:
                    t = Transaccion()
                    t.tipoTrasaccion = 'debito'
                    t.fecha = datetime.datetime.now()
                    t.hora = datetime.datetime.now()
                    t.monto = monto
                    t.save()

                    l = Log()

                    u = Usuario.objects.get(usuario=request.user.get_username())

                    l.idTrasaccion = t
                    l.idCuenta = cDestino
                    l.idPrograma = ""
                    l.idUsuario = u
                    l.fecha = datetime.datetime.now()
                    l.hora = datetime.datetime.now()
                    l.saldo_inicial = cDestino.saldo
                    l.saldo = cDestino.saldo
                    l.debito = monto
                    l.credito = 0
                    l.autorizacion = 0
                    l.rechazo = 1
                    l.razonRechazo = 'La cuenta no tiene suficientes fondos'
                    l.save()

                    messages.add_message(request, messages.INFO, 'La cuenta no tiene suficientes fondos')

                    form = TransferenciaCuentasForm()
        return render(request, 'Caja/transferencia.html', {'form': form,'transferencia':t})
    else:
        form = TransferenciaCuentasForm()

    return render(request, 'Caja/transferencia.html', {'form': form})

@login_required(login_url='/login')
def crearEstadoTarjeta(request):
    if request.method == 'POST':
        form = CrearEstadoTarjetaForm(request.POST)

        if form.is_valid():
            form.save()
            form = CrearEstadoTarjetaForm()
            messages.add_message(request, messages.INFO, 'El estado de tarjeta ha sido creada')
            return render(request, 'Tarjetas/TipoEstado.html', {'form': form})
    else:
        form = CrearEstadoTarjetaForm()

    return render(request, 'Tarjetas/TipoEstado.html', {'form': form})

@login_required(login_url='/login')
def crearNota(request):
    if request.method == 'POST':
        form = NotasForm(request.POST)

        if form.is_valid():
            form.save()
            form = NotasForm()
            messages.add_message(request, messages.INFO, 'La nota ha sido creada')
            return render(request, 'Notas/Crear.html', {'form': form})
    else:
        form = NotasForm()

    return render(request, 'Notas/Crear.html', {'form': form})

@login_required(login_url='/login')
def asignarUsuarioLote(request):
    if request.method == 'POST':
        form = AsigUsuarioLoteForm(request.POST)
        idform = form.data['idUsuario']
        form.data = form.data.copy()
        form.data['idUsuario'] = Usuario.objects.filter(usuario=idform).values_list('id', flat=True)
        if form.is_valid():
            form.save()
            form = AsigUsuarioLoteForm()
            form.fields["idLote"].queryset = Lote.objects.all().values_list('id',flat=True)  # se llena el form con los valores
            form.fields["idUsuario"].queryset = Usuario.objects.all().values_list('usuario',flat=True)  # se llena el form con los valores
            messages.add_message(request, messages.INFO, 'El lote ha sido asignado al usuario')
            return render(request, 'Lote/AsignarUsuarioLote.html', {'form': form})
    else:
        form = AsigUsuarioLoteForm()
    form.fields["idLote"].queryset = Lote.objects.all().values_list('id',flat=True)  # se llena el form con los valores
    form.fields["idUsuario"].queryset = Usuario.objects.all().values_list('usuario',flat=True)  # se llena el form con los valores
    return render(request, 'Lote/AsignarUsuarioLote.html', {'form': form})

@login_required(login_url='/login')
def asignarAfiliadoLote(request):
    if request.method == 'POST':
        form = AsigAfiliadoLoteForm(request.POST)
        idform = form.data['idAfiliado']
        form.data = form.data.copy()
        form.data['idAfiliado'] = Afiliado.objects.filter(nombre=idform).values_list('id', flat=True)
        if form.is_valid():
            form.save()
            form = AsigAfiliadoLoteForm()
            form.fields["idLote"].queryset = Lote.objects.all().values_list('id',flat=True)  # se llena el form con los valores
            form.fields["idAfiliado"].queryset = Afiliado.objects.all().values_list('nombre',flat=True)  # se llena el form con los valores
            messages.add_message(request, messages.INFO, 'El lote ha sido asignado al afiliado')
            return render(request, 'Lote/AsignarAfiliadoLote.html', {'form': form})
    else:
        form = AsigAfiliadoLoteForm()
    form.fields["idLote"].queryset = Lote.objects.all().values_list('id',flat=True)  # se llena el form con los valores
    form.fields["idAfiliado"].queryset = Afiliado.objects.all().values_list('nombre',flat=True)  # se llena el form con los valores
    return render(request, 'Lote/AsignarAfiliadoLote.html', {'form': form})


@login_required(login_url='/login')
def crearLote(request):
    if request.method == 'POST':
        form = LoteForm(request.POST)

        if form.is_valid():
            form.save()
            form = LoteForm()
            messages.add_message(request, messages.INFO, 'El lote ha sido creado')
            return render(request, 'Lote/Crear.html', {'form': form})
    else:
        form = LoteForm()

    return render(request, 'Lote/Crear.html', {'form': form})

@login_required(login_url='/login')
def BuscarCuenta2(request):
    if request.method == 'POST':
        form = BuscarCuentaForm(request.POST)
        if form.is_valid():

            return render(request,'Autorizacion/Buscar.html',{'form':form})
    else:
        form = BuscarCuentaForm()

    return render(request,'Autorizacion/Buscar.html',{'form':form})

@login_required(login_url='/login')
def BuscarCuentaAjax2(request):
    if request.method == 'POST':
        search_text = int(request.POST['search_text'])
    else:
        search_text = 0

    cuentas = Cuenta.objects.filter(id__startswith=search_text)

    return render(request,'Autorizacion/busqueda_ajax.html',{'cuentas':cuentas})
@login_required(login_url='/login')
def retirar(request,id):
    if request.method =='POST':
        c = Cuenta.objects.get(id=id)
        saldoInicial = c.saldo
        form = RetirarEfectivo(request.POST)
        if form.is_valid():
            cantidad = float(form.data['cantidad'])
            if cantidad >= c.saldo:
                messages.add_message(request, messages.INFO, 'El monto no puede ser mayor al saldo')

                t = Transaccion()
                t.tipoTrasaccion = 'credito'
                t.fecha = datetime.datetime.now()
                t.hora = datetime.datetime.now()
                t.monto = cantidad
                t.save()

                l = Log()

                u = Usuario.objects.get(usuario=request.user.get_username())

                l.idTrasaccion = t
                l.idCuenta = c
                l.idPrograma = ""
                l.idUsuario = u
                l.fecha = datetime.datetime.now()
                l.hora = datetime.datetime.now()
                l.saldo_inicial = c.saldo
                l.saldo = c.saldo
                l.debito = cantidad
                l.credito = 0
                l.autorizacion = 0
                l.rechazo = 1
                l.razonRechazo = 'El monto no puede ser mayor al saldo'
                l.save()
            else:
                messages.add_message(request, messages.INFO, 'El retiro ha sido realizado')
                c.saldo = c.saldo + cantidad
                c.save()

                t = Transaccion()
                t.tipoTrasaccion = 'credito'
                t.fecha = datetime.datetime.now()
                t.hora = datetime.datetime.now()
                t.monto = cantidad
                t.save()

                l = Log()

                u = Usuario.objects.get(usuario=request.user.get_username())

                l.idTrasaccion = t
                l.idCuenta = c
                l.idPrograma = ""
                l.idUsuario = u
                l.fecha = datetime.datetime.now()
                l.hora = datetime.datetime.now()
                l.saldo_inicial = saldoInicial
                l.saldo = c.saldo
                l.debito = cantidad
                l.credito = 0
                l.autorizacion = 1
                l.rechazo = 0
                l.razonRechazo = ''
                l.save()

                form = RetirarEfectivo()
        return render(request, 'Autorizacion/Retiro.html',{'form':form, 'cuenta':c})
    else:
        c = Cuenta()
        c = Cuenta.objects.get(id = id)
        form = RetirarEfectivo()
    return render(request, 'Autorizacion/Retiro.html',{'form':form, 'cuenta':c})

@login_required(login_url='/login')
def declararCambios(request):
    if request.method == 'POST':
        form = DeclaCambioForm(request.POST)
        idform = form.data['idEstado']
        form.data = form.data.copy()
        form.data['idEstado'] = TipoEstado.objects.filter(tipoEstado=idform).values_list('id', flat=True)
        if form.is_valid():
            form.save()
            form = DeclaCambioForm()
            form.fields["idEstado"].queryset = TipoEstado.objects.all().values_list('tipoEstado',flat=True)  # se llena el form con los valores
            form.fields["idTarjeta"].queryset = Tarjeta.objects.all().values_list('id',flat=True)  # se llena el form con los valores
            messages.add_message(request, messages.INFO, 'La tarjeta ha sido declarada')
            return render(request, 'Tarjetas/DeclaracionCambios.html', {'form': form})
    else:
        form = DeclaCambioForm()
    form.fields["idEstado"].queryset = TipoEstado.objects.all().values_list('tipoEstado',flat=True)  # se llena el form con los valores
    form.fields["idTarjeta"].queryset = Tarjeta.objects.all().values_list('id',flat=True)  # se llena el form con los valores
    return render(request, 'Tarjetas/DeclaracionCambios.html', {'form': form})


@login_required(login_url='/login')
def consultar_Saldo(request):
    if request.method == 'POST':
        form = BuscarCuentaForm(request.POST)
        if form.is_valid():
            numerocuenta = form.data['idCuenta']
            try:
                saldo = Cuenta.objects.get(id=numerocuenta)

                return render(request, 'Cuentas/ListaCuentas.html', {'saldo': saldo})
            except:
                return render(request, 'Cuentas/ListaCuentas.html')

    else:
        form = BuscarCuentaForm()

    return render(request, 'Cuentas/ConsultaSaldo.html', {'form': form})

@login_required(login_url='/login')
def asignarInteresEmisor(request):
    if request.method == 'POST':
        form = AsigInteresEmisorForm(request.POST)
        idform = form.data['idEmisor']
        form.data = form.data.copy()
        form.data['idEmisor'] = Emisor.objects.filter(nombre=idform).values_list('id', flat=True)

        if form.is_valid():
            form.save()
            form = AsigInteresEmisorForm()
            form.fields["idEmisor"].queryset = Emisor.objects.all().values_list('nombre',flat=True)  # se llena el form con los valores
            messages.add_message(request, messages.INFO, 'El Interes ha sido asignado al emisor')
            return render(request, 'Emisor/AsignarInteres.html', {'form': form})
    else:
        form = AsigInteresEmisorForm()
    form.fields["idEmisor"].queryset = Emisor.objects.all().values_list('nombre',flat=True)  # se llena el form con los valores
    return render(request, 'Emisor/AsignarInteres.html', {'form': form})

@login_required(login_url='/login')
def crearEmisor(request):
    if request.method == 'POST':
        form = EmisorForm(request.POST)

        if form.is_valid():
            form.save()
            form = EmisorForm()
            messages.add_message(request, messages.INFO, 'El Emisor ha sido creado')
            return render(request, 'Emisor/Crear.html', {'form': form})
    else:
        form = EmisorForm()

    return render(request, 'Emisor/Crear.html', {'form': form})

@login_required(login_url='/login')
def asignarInteresCuenta(request):
    if request.method == 'POST':
        form = AsigInteresCuentaForm(request.POST)

        if form.is_valid():
            form.save()
            form = AsigInteresCuentaForm()
            messages.add_message(request, messages.INFO, 'El Interes ha sido asignado a la cuenta')
            form.fields["idCuenta"].queryset = Cuenta.objects.all().values_list('id',flat=True)  # se llena el form con los valores
            return render(request, 'Cuentas/AsignarInteres.html', {'form': form})
    else:
        form = AsigInteresCuentaForm()
    form.fields["idCuenta"].queryset = Cuenta.objects.all().values_list('id',flat=True)  # se llena el form con los valores
    return render(request, 'Cuentas/AsignarInteres.html', {'form': form})

@login_required(login_url='/login')
def crearRol(request):
    if request.method == 'POST':
        form = RolForm(request.POST)

        if form.is_valid():
            form.save()
            form = RolForm()
            messages.add_message(request, messages.INFO, 'El Rol ha sido creado')
            return render(request, 'Rol/Crear.html', {'form': form})
    else:
        form = RolForm()

    return render(request, 'Rol/Crear.html', {'form': form})

@login_required(login_url='/login')
def autorizarRol(request):
    if request.method == 'POST':
        form = AutorizarRolForm(request.POST)

         # se coloca el valor valido en el form, es decir el id en vez del nombre
        idform = form.data['idRol']
        form.data = form.data.copy()
        form.data['idRol'] = Rol.objects.filter(rol=idform).values_list('id', flat=True)

        if form.is_valid():
            form.save()
            form = AutorizarRolForm()
            messages.add_message(request, messages.INFO, 'La autorizacion ha sido asignada')
            form.fields["idRol"].queryset = Rol.objects.all().values_list('rol',flat=True)  # se llena el form con los valoress
            return render(request, 'Rol/Autorizacion.html', {'form': form})

    else:
        form = AutorizarRolForm()
        form.fields["idRol"].queryset = Rol.objects.all().values_list('rol',flat=True)  # se llena el form con los valores
    return render(request, 'Rol/Autorizacion.html', {'form': form})

@login_required(login_url='/login')
def privilegioRol(request):

    if request.method == 'POST':
        form = PrivilegioRolForm(request.POST)

         # se coloca el valor valido en el form, es decir el id en vez del nombre
        idform = form.data['idRol']
        form.data = form.data.copy()
        form.data['idRol'] = Rol.objects.filter(rol=idform).values_list('id', flat=True)

        if form.is_valid():
            form.save()
            form = PrivilegioRolForm()
            messages.add_message(request, messages.INFO, 'El privilegio ha sido asignado')
            form.fields["idRol"].queryset = Rol.objects.all().values_list('rol',flat=True)  # se llena el form con los valores
            return render(request, 'Rol/Privilegio.html', {'form': form})

    else:
        form = PrivilegioRolForm()
        form.fields["idRol"].queryset = Rol.objects.all().values_list('rol',flat=True)  # se llena el form con los valores
    return render(request, 'Rol/Privilegio.html', {'form': form})

@login_required(login_url='/login')
def buscarRol(request):
    u = None
    if request.method == 'POST':
        form = Buscar_RolForm(request.POST)
        idform = form.data['idRol']
        form.data = form.data.copy()
        form.data['idRol'] = Rol.objects.filter(rol=idform).values_list('id', flat=True)
        if form.is_valid():
            idr = form.data['idRol']
            u = Rol.objects.get(id=idr)
            form = Buscar_RolForm()
            return render(request, 'Rol/Buscar.html', {'form': form, 'Rol': u})
    else:
        form = Buscar_RolForm()
    return render(request, 'Rol/Buscar.html', {'form': form, 'Rol': u})

@login_required(login_url='/login')
def editarRol(request, id):
    if request.method == 'POST':
        u = Rol.objects.get(id=id)
        form = RolForm(request.POST, instance=u)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'El rol ha sido editado')
            form = Buscar_RolForm()
            return render(request, 'Rol/Buscar.html', {'form': form})
    else:
        form = RolForm()
        try:
            u = Rol.objects.get(id=id)
        except:
            messages.add_message(request, messages.INFO, 'EL tipo afiliado no existe en la base de datos')
            return render(request, 'Rol/Editar.html', {'form': form, 'Rol': u})
        form = RolForm(instance=u)

    idRol = u.id
    return render(request, 'Rol/Editar.html', {'form': form, 'idRol': idRol})

@login_required(login_url='/login')
def eliminarRol(request, id):
    Rol.objects.get(id=id).delete()
    messages.add_message(request, messages.INFO, 'El rol ha sido eliminado')
    form = Buscar_RolForm()
    return render(request, 'Rol/Buscar.html', {'form': form})

@login_required(login_url='/login')
def crearTipoTarjeta(request):
    if request.method == 'POST':
        form = TipoTarjetaForm(request.POST)

        if form.is_valid():
            form.save()
            form = TipoTarjetaForm()
            messages.add_message(request, messages.INFO, 'El tipo de tarjeta ha sido creado')
            return render(request, 'TipoTarjeta/CrearTT.html', {'form': form})
    else:
        form = TipoTarjetaForm()

    return render(request, 'TipoTarjeta/CrearTT.html', {'form': form})

@login_required(login_url='/login')
def buscarTipoTarjeta(request):
    u = None
    if request.method == 'POST':
        form = Buscar_TTarjetaForm(request.POST)
        idform = form.data['idTT']
        form.data = form.data.copy()
        form.data['idTT'] = TipoTarjeta.objects.filter(tipoTarjeta=idform).values_list('id', flat=True)
        if form.is_valid():
            idr = form.data['idTT']
            u = TipoTarjeta.objects.get(id=idr)
            form = Buscar_TTarjetaForm()
            return render(request, 'TipoTarjeta/BuscarTT.html', {'form': form, 'TT': u})
    else:
        form = Buscar_TTarjetaForm()
    return render(request, 'TipoTarjeta/BuscarTT.html', {'form': form, 'TT': u})

@login_required(login_url='/login')
def editarTipoTarjeta(request, id):
    if request.method == 'POST':
        u = TipoTarjeta.objects.get(id=id)
        form = TipoTarjetaForm(request.POST, instance=u)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'El tipo de tarjeta ha sido editado')
            form = Buscar_TTarjetaForm()
            return render(request, 'TipoTarjeta/BuscarTT.html', {'form': form})
    else:
        form = ()
        try:
            u = TipoTarjeta.objects.get(id=id)
        except:
            messages.add_message(request, messages.INFO, 'EL tipo de tarjeta no existe en la base de datos')
            return render(request, 'TipoTarjeta/EditarTT.html', {'form': form, 'TT': u})
        form = TipoTarjetaForm(instance=u)

    idTT = u.id
    return render(request, 'TipoTarjeta/EditarTT.html', {'form': form, 'idTT': idTT})

@login_required(login_url='/login')
def eliminarTipoTarjeta(request, id):
    TipoTarjeta.objects.get(id=id).delete()
    messages.add_message(request, messages.INFO, 'El tipo de tarjeta ha sido eliminado')
    form = Buscar_TTarjetaForm()
    return render(request, 'TipoTarjeta/BuscarTT.html', {'form': form})

@login_required(login_url='/login')
def buscarEmisor(request):
    u = None
    if request.method == 'POST':
        form = Buscar_EmisorForm(request.POST)
        idform = form.data['idEmisor']
        form.data = form.data.copy()
        form.data['idEmisor'] = Emisor.objects.filter(nombre=idform).values_list('id', flat=True)
        if form.is_valid():
            idr = form.data['idEmisor']
            u = Emisor.objects.get(id=idr)
            form = Buscar_EmisorForm()
            return render(request, 'Emisor/Buscar.html', {'form': form, 'Emisor': u})
    else:
        form = Buscar_EmisorForm()
    return render(request, 'Emisor/Buscar.html', {'form': form, 'Emisor': u})

@login_required(login_url='/login')
def BuscarEmisorAjax(request):
    if request.method == 'POST':
        search_text = request.POST['search_text']
    else:
        search_text = 0

    emisores = Emisor.objects.filter(nombre__istartswith=search_text)

    return render(request, 'Emisor/busqueda_ajax.html', {'emisores': emisores})


@login_required(login_url='/login')
def editarEmisor(request, id):
    if request.method == 'POST':
        u = Emisor.objects.get(id=id)
        form = EmisorForm(request.POST, instance=u)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'El Emisor ha sido editado')
            form = Buscar_EmisorForm()
            return render(request, 'Emisor/Buscar.html', {'form': form})
    else:
        form = EmisorForm()
        try:
            u = Emisor.objects.get(id=id)
        except:
            messages.add_message(request, messages.INFO, 'EL tipo afiliado no existe en la base de datos')
            return render(request, 'Emisor/Editar.html', {'form': form, 'Emisor': u})
        form = EmisorForm(instance=u)

    idEmisor = u.id
    return render(request, 'Emisor/Editar.html', {'form': form, 'idEmisor': idEmisor})

@login_required(login_url='/login')
def eliminarEmisor(request, id):
    Emisor.objects.get(id=id).delete()
    messages.add_message(request, messages.INFO, 'El Emisor ha sido eliminado')
    form = Buscar_EmisorForm()
    return render(request, 'Emisor/Buscar.html', {'form': form})

@login_required(login_url='/login')
def buscarPrivilegio(request):
    u = None
    if request.method == 'POST':
        form = Buscar_PrivilegioForm(request.POST)
        idform = form.data['idPrivilegio']
        form.data = form.data.copy()
        form.data['idPrivilegio'] = Privilegio.objects.filter(privilegio=idform).values_list('id', flat=True)
        if form.is_valid():
            idr = form.data['idPrivilegio']
            u = Privilegio.objects.get(id=idr)
            form = Buscar_PrivilegioForm()
            return render(request, 'Rol/BuscarPrivilegio.html', {'form': form, 'Privilegio': u})
    else:
        form = Buscar_PrivilegioForm()
    return render(request, 'Rol/BuscarPrivilegio.html', {'form': form, 'Privilegio': u})

@login_required(login_url='/login')
def editarPrivilegio(request, id):
    if request.method == 'POST':
        u = Privilegio.objects.get(id=id)
        form = PrivilegioRolForm(request.POST, instance=u)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'El Privilegio ha sido editado')
            form = Buscar_PrivilegioForm()
            return render(request, 'Rol/BuscarPrivilegio.html', {'form': form})
    else:
        form = PrivilegioRolForm()
        try:
            u = Privilegio.objects.get(id=id)
        except:
            messages.add_message(request, messages.INFO, 'EL tipo afiliado no existe en la base de datos')
            return render(request, 'Rol/EditarPrivilegio.html', {'form': form, 'Privilegio': u})
        form = PrivilegioRolForm(instance=u)

    idPrivilegio = u.id
    return render(request, 'Rol/EditarPrivilegio.html', {'form': form, 'idPrivilegio': idPrivilegio})

@login_required(login_url='/login')
def eliminarPrivilegio(request, id):
    Privilegio.objects.get(id=id).delete()
    messages.add_message(request, messages.INFO, 'El Privilegio ha sido eliminado')
    form = Buscar_PrivilegioForm()
    return render(request, 'Rol/BuscarPrivilegio.html', {'form': form})

@login_required(login_url='/login')
def buscarAutorizacion(request):
    u = None
    if request.method == 'POST':
        form = Buscar_AutorizacionForm(request.POST)
        idform = form.data['idAutorizacion']
        form.data = form.data.copy()
        form.data['idAutorizacion'] = Autorizacion.objects.filter(autorizacion=idform).values_list('id', flat=True)
        if form.is_valid():
            idr = form.data['idAutorizacion']
            u = Autorizacion.objects.get(id=idr)
            form = Buscar_AutorizacionForm()
            return render(request, 'Rol/BuscarAutorizacion.html', {'form': form, 'Autorizacion': u})
    else:
        form = Buscar_AutorizacionForm()
    return render(request, 'Rol/BuscarAutorizacion.html', {'form': form, 'Autorizacion': u})

@login_required(login_url='/login')
def editarAutorizacion(request, id):
    if request.method == 'POST':
        u = Autorizacion.objects.get(id=id)
        form = AutorizarRolForm(request.POST, instance=u)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'El Autorizacion ha sido editado')
            form = Buscar_AutorizacionForm()
            return render(request, 'Rol/BuscarAutorizacion.html', {'form': form})
    else:
        form = AutorizarRolForm()
        try:
            u = Autorizacion.objects.get(id=id)
        except:
            messages.add_message(request, messages.INFO, 'EL tipo afiliado no existe en la base de datos')
            return render(request, 'Rol/EditarAutorizacion.html', {'form': form, 'Autorizacion': u})
        form = AutorizarRolForm(instance=u)

    idAutorizacion = u.id
    return render(request, 'Rol/EditarAutorizacion.html', {'form': form, 'idAutorizacion': idAutorizacion})

@login_required(login_url='/login')
def eliminarAutorizacion(request, id):
    Autorizacion.objects.get(id=id).delete()
    messages.add_message(request, messages.INFO, 'El Autorizacion ha sido eliminado')
    form = Buscar_AutorizacionForm()
    return render(request, 'Rol/BuscarAutorizacion.html', {'form': form})

@login_required(login_url='/login')
def buscarTipoEstado(request):
    u = None
    if request.method == 'POST':
        form = Buscar_TipoEstadoForm(request.POST)
        idform = form.data['idTipoEstado']
        form.data = form.data.copy()
        form.data['idTipoEstado'] = TipoEstado.objects.filter(tipoEstado=idform).values_list('id', flat=True)
        if form.is_valid():
            idr = form.data['idTipoEstado']
            u = TipoEstado.objects.get(id=idr)
            form = Buscar_TipoEstadoForm()
            return render(request, 'Tarjetas/BuscarTE.html', {'form': form, 'TipoEstado': u})
    else:
        form = Buscar_TipoEstadoForm()
    return render(request, 'Tarjetas/BuscarTE.html', {'form': form, 'TipoEstado': u})

@login_required(login_url='/login')
def editarTipoEstado(request, id):
    if request.method == 'POST':
        u = TipoEstado.objects.get(id=id)
        form = CrearEstadoTarjetaForm(request.POST, instance=u)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'El TipoEstado ha sido editado')
            form = Buscar_TipoEstadoForm()
            return render(request, 'Tarjetas/BuscarTE.html', {'form': form})
    else:
        form = CrearEstadoTarjetaForm()
        try:
            u = TipoEstado.objects.get(id=id)
        except:
            messages.add_message(request, messages.INFO, 'EL tipo afiliado no existe en la base de datos')
            return render(request, 'Tarjetas/EditarTE.html', {'form': form, 'TipoEstado': u})
        form = CrearEstadoTarjetaForm(instance=u)

    idTipoEstado = u.id
    return render(request, 'Tarjetas/EditarTE.html', {'form': form, 'idTipoEstado': idTipoEstado})

@login_required(login_url='/login')
def eliminarTipoEstado(request, id):
    TipoEstado.objects.get(id=id).delete()
    messages.add_message(request, messages.INFO, 'El TipoEstado ha sido eliminado')
    form = Buscar_TipoEstadoForm()
    return render(request, 'Tarjetas/BuscarTE.html', {'form': form})

@login_required(login_url='/login')
def buscarTipoCuenta(request):
    u = None
    if request.method == 'POST':
        form = Buscar_TipoCuentaForm(request.POST)
        idform = form.data['idTipoCuenta']
        form.data = form.data.copy()
        form.data['idTipoCuenta'] = TipoCuenta.objects.filter(tipoCuenta=idform).values_list('id', flat=True)
        if form.is_valid():
            idr = form.data['idTipoCuenta']
            u = TipoCuenta.objects.get(id=idr)
            form = Buscar_TipoCuentaForm()
            return render(request, 'Cuentas/BuscarTC.html', {'form': form, 'TipoCuenta': u})
    else:
        form = Buscar_TipoCuentaForm()
    return render(request, 'Cuentas/BuscarTC.html', {'form': form, 'TipoCuenta': u})

@login_required(login_url='/login')
def editarTipoCuenta(request, id):
    if request.method == 'POST':
        u = TipoCuenta.objects.get(id=id)
        form = TipoCuentaForm(request.POST, instance=u)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'El TipoCuenta ha sido editado')
            form = Buscar_TipoCuentaForm()
            return render(request, 'Cuentas/BuscarTC.html', {'form': form})
    else:
        form = TipoCuentaForm()
        try:
            u = TipoCuenta.objects.get(id=id)
        except:
            messages.add_message(request, messages.INFO, 'EL tipo afiliado no existe en la base de datos')
            return render(request, 'Cuentas/EditarTC.html', {'form': form, 'TipoCuenta': u})
        form = TipoCuentaForm(instance=u)

    idTipoCuenta = u.id
    return render(request, 'Cuentas/EditarTC.html', {'form': form, 'idTipoCuenta': idTipoCuenta})

@login_required(login_url='/login')
def eliminarTipoCuenta(request, id):
    TipoCuenta.objects.get(id=id).delete()
    messages.add_message(request, messages.INFO, 'El TipoCuenta ha sido eliminado')
    form = Buscar_TipoCuentaForm()
    return render(request, 'Cuentas/BuscarTC.html', {'form': form})