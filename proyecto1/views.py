from django.shortcuts import render
# Create your views here.

from .forms import *
from django.http import HttpResponse

from django.contrib import messages #para emitir aletrs
def index(request):
    return render(request,'Index.html')

def indexClientes(request):
    messages.add_message(request, messages.INFO, 'Hello world.')
    return  render(request,'Clientes/Index.html')


def indexCuentas(request):
    return  render(request,'Cuentas/Index.html')

def indexTarjetas(request):
    return  render(request,'Tarjetas/Index.html')

def indexAfiliado(request):
    return  render(request,'Afiliado/Index.html')

def indexTipoAfiliado(request):
    return  render(request,'TipoAfiliado/Index.html')

def insertarClientes(request):
    if request.method =='POST':
        form = UsuarioForm(request.POST)

        if form.is_valid():
            usuario = form.save()       #con esto no hay necesidad de igualar los datos ya se salva a la base de datos

            return HttpResponse('<h1>Cliente insertado</h1>')
    else:
        form = UsuarioForm()

    return render(request,'Clientes/Insertar.html',{'form':form})

def Bloquear_Clientes(request,id):
    u = Usuario.objects.get(id=id)
    u.bloqueado = True
    u.save()
    return HttpResponse('<h1>Usuario Bloqueado</h1>')


def Buscar_Clientes(request):
    form = BuscarCliente(request.POST)
    u = None
    if form.is_valid():
        try:
            u = Usuario.objects.get(id=form.cleaned_data['id'])
        except :
            return HttpResponse('<h1>El usuario no existe en la Base de Datos</h1>')

    usuario = BuscarCliente()
    return render(request,'Clientes/Buscar.html',{'form':usuario,'usuario':u})

def Eliminar_Clientes(request,id):
    Usuario.objects.get(id=id).delete()
    return HttpResponse('<h1>Usuario Eliminado</h1>')



def crearCuenta(request):
    if request.method =='POST':
        form = CuentaForm(request.POST)

        if form.is_valid():
            c = Cuenta()
            c.tipo = form.cleaned_data['tipo']
            c.limite = form.cleaned_data['limite']
            c.fechaCreacion = form.cleaned_data['fechaCreacion']
            c.save()
            return HttpResponse('<h1>Cuenta Insertada</h1>')
    else:
        form = CuentaForm()

    return render(request,'Cuentas/Crear.html',{'form':form})

def asignarCuenta(request):
    if request.method =='POST':
        form = AsigCuentaForm(request.POST)

        if form.is_valid():
            a = AsignacionCuenta()
            a.idUsuario = form.cleaned_data['idUsuario']
            a.idCuenta = form.cleaned_data['idCuenta']
            a.save()
            return HttpResponse('<h1>Cuenta Asignada</h1>')
    else:
        form = AsigCuentaForm()

    return render(request,'Cuentas/AsignarCuenta.html',{'form':form})

def crearTarjeta(request):
    if request.method =='POST':
        form = TarjetaForm(request.POST)

        if form.is_valid():
            t = Tarjeta()
            t.noTarjeta = form.cleaned_data['noTarjeta']
            t.tipo = form.cleaned_data['tipo']
            t.limite = form.cleaned_data['limite']
            t.fechaCorte = form.cleaned_data['fechaCorte']
            t.fechaPago = form.cleaned_data['fechaPago']
            t.save()
            return HttpResponse('<h1>Tarjeta Creada</h1>')
    else:
        form = TarjetaForm()

    return render(request,'Tarjetas/CrearTarjeta.html',{'form':form})

def asignarTarjeta(request):
    if request.method =='POST':
        form = AsigTarjetaForm(request.POST)

        if form.is_valid():
            a = AsignacionTarjeta()
            a.idCuenta = form.cleaned_data['idCuenta']
            a.noTarjeta = form.cleaned_data['noTarjeta']
            a.fechaAsignacion = form.cleaned_data['fechaAsignacion']
            a.save()
            return HttpResponse('<h1>Tarjeta Asignada</h1>')
    else:
        form = AsigTarjetaForm()

    return render(request,'Tarjetas/AsignarTarjeta.html',{'form':form})

def editarClientes(request,id):
    if request.method =='POST':
        u = Usuario.objects.get(id=id)
        form = UsuarioForm(request.POST,instance=u)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>El usuario ha sido editado</h1>')
    else:
        u = Usuario()
        try:
            u = Usuario.objects.get(id=id)
        except:
            return HttpResponse('<h1>El usuario no existe en la Base de Datos</h1>')
        form = UsuarioForm(instance=u)

    idusuario = u.id
    return render(request,'Clientes/Editar.html',{'form':form,'idusuario':idusuario})

def insertarAfiliado(request):
    if request.method =='POST':
        form = AfiliadoForm(request.POST)

        if form.is_valid():
            t = Afiliado()
            t.nombre = form.cleaned_data['nombre']
            t.direccion = form.cleaned_data['direccion']
            t.telefono = form.cleaned_data['telefono']
            t.correo = form.cleaned_data['correo']
            t.save()
            return HttpResponse('<h1>Afiliado insertado</h1>')
    else:
        form = AfiliadoForm()

    return render(request,'Afiliado/Insertar.html',{'form':form})

def Buscar_Afiliados(request):
    form = BuscarCliente(request.POST)
    u = None
    if form.is_valid():
        try:
            u = Afiliado.objects.get(id=form.cleaned_data['id'])
        except :
            return HttpResponse('<h1>El afiliado no existe en la Base de Datos</h1>')

    afiliado = BuscarCliente()
    return render(request,'Afiliado/Buscar.html',{'form':afiliado,'afiliado':u})

def Eliminar_Afiliados(request,id):
    Afiliado.objects.get(id=id).delete()
    return HttpResponse('<h1>Afiliado Eliminado</h1>')

def Eliminar_TipoAfiliados(request,id):
    TipoAfiliado.objects.get(id=id).delete()
    return HttpResponse('<h1>Tipo Afiliado Eliminado</h1>')

def Bloquear_Afiliados(request,id):
    u = Afiliado.objects.get(id=id)
    u.bloqueado = True
    u.save()
    return HttpResponse('<h1>Afiliado Bloqueado</h1>')

def Bloquear_TipoAfiliados(request,id):
    u = TipoAfiliado.objects.get(id=id)
    u.bloqueado = True
    u.save()
    return HttpResponse('<h1>Tipo Afiliado Bloqueado</h1>')

def editarAfiliados(request,id):
    if request.method =='POST':
        u = Afiliado.objects.get(id=id)
        form = AfiliadoForm(request.POST,instance=u)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>El afiliado ha sido editado</h1>')
    else:
        u = Afiliado()
        try:
            u = Afiliado.objects.get(id=id)
        except:
            return HttpResponse('<h1>El afiliado no existe en la Base de Datos</h1>')
        form = AfiliadoForm(instance=u)

    idafiliado = u.id
    return render(request,'Afiliado/Editar.html',{'form':form,'idafiliado':idafiliado})

def insertarTipoAfiliado(request):
    if request.method =='POST':
        form = TipoAfiliadoForm(request.POST)

        if form.is_valid():
            t = TipoAfiliado()
            t.nombre = form.cleaned_data['nombre']
            t.descripcion = form.cleaned_data['descripcion']
            t.porcentaje = form.cleaned_data['porcentaje']
            t.save()
            return HttpResponse('<h1>Tipo afiliado insertado</h1>')
    else:
        form = TipoAfiliadoForm()

    return render(request,'TipoAfiliado/Insertar.html',{'form':form})


def BuscarTipoAfiliado(request):
    form = BuscarCliente(request.POST)
    t = None
    if form.is_valid():
        try:
            t = TipoAfiliado.objects.get(id=form.cleaned_data['id'])
        except :
            return HttpResponse('<h1>El Tipo de afiliado no existe en la Base de Datos</h1>')

    buscartipoafiliado = BuscarCliente()
    return render(request,'TipoAfiliado/Buscar.html',{'form':buscartipoafiliado,'TipoAfiliado':t})
##
def editarTipoAfiliados(request,id):
    if request.method =='POST':
        u = TipoAfiliado.objects.get(id=id)
        form = TipoAfiliadoForm(request.POST,instance=u)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>El tipo afiliado ha sido editado</h1>')
    else:
        u = TipoAfiliado()
        try:
            u = TipoAfiliado.objects.get(id=id)
        except:
            return HttpResponse('<h1>El tipo afiliado no existe en la Base de Datos</h1>')
        form = TipoAfiliadoForm(instance=u)

    idTipoafiliado = u.id
    return render(request,'TipoAfiliado/Editar.html',{'form':form,'idTipoafiliado':idTipoafiliado})
