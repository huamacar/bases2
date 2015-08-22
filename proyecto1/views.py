from django.shortcuts import render
from django.template import RequestContext
from proyecto1.models import *
from django.shortcuts import  render_to_response
from django.http import HttpResponseRedirect
# Create your views here.

from .forms import UsuarioForm
from .forms import CuentaForm
from .forms import AsigCuentaForm
from .forms import TarjetaForm
from .forms import AsigTarjetaForm
from .forms import *
from django import forms
from django.http import HttpResponse
from django.shortcuts import redirect

def index(request):
    return render(request,'Index.html')

def indexClientes(request):
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
            u = Usuario()
            u.nombre = form.cleaned_data['nombre']
            u.direccion = form.cleaned_data['direccion']
            u.telefono = form.cleaned_data['telefono']
            u.correo = form.cleaned_data['correo']
            u.fechaNacimiento = form.cleaned_data['fechaNacimiento']
            u.profesion = form.cleaned_data['profesion']
            u.genero = form.cleaned_data['genero']
            u.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = UsuarioForm()

    return render(request,'Clientes/Insertar.html',{'form':form})


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
            return HttpResponseRedirect('/thanks/')
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
            return HttpResponseRedirect('/thanks/')
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
            return HttpResponseRedirect('/thanks/')
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
            return HttpResponseRedirect('/thanks/')
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
            return HttpResponseRedirect('/thanks/')
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
            return HttpResponseRedirect('/thanks/')
    else:
        form = TipoAfiliadoForm()

    return render(request,'TipoAfiliado/Insertar.html',{'form':form})


def blabla(request):
    input = request.GET.get('q')
    try:
        query = 1
    except ValueError:
        query = None
        results = None
    if query:
        u = Usuario.objects.get(id=query)

    context = RequestContext(request)
    return render_to_response('Index.html',{"results":u,},context_instance=context)
