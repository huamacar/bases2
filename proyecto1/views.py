from django.shortcuts import render
from django.template import RequestContext
from proyecto1.models import Usuario
from proyecto1.models import Cuenta
from proyecto1.models import AsignacionCuenta
from proyecto1.models import Tarjeta
from proyecto1.models import AsignacionTarjeta
from django.shortcuts import  render_to_response
from django.http import HttpResponseRedirect
# Create your views here.

from .forms import UsuarioForm
from .forms import CuentaForm
from .forms import AsigCuentaForm
from .forms import TarjetaForm
from .forms import AsigTarjetaForm
from .forms import EditarUsuarioForm
from .forms import *
from django import forms
from django.http import HttpResponse

def index(request):
    return render(request,'Index.html')

def indexClientes(request):
    return  render(request,'Clientes/Index.html')

def indexCuentas(request):
    return  render(request,'Cuentas/Index.html')

def indexTarjetas(request):
    return  render(request,'Tarjetas/Index.html')

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
    u = Usuario()
    if form.is_valid():
        u = Usuario.objects.get(nombre=form.cleaned_data['nombre'])
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

def editarClientes(request):
    if request.method =='POST':
        form = EditarUsuarioForm(request.POST)

        if form.is_valid():
            if form.cleaned_data['eliminar'] == True:
                u = Usuario.objects.get(nombre=form.cleaned_data['nombreAnterior'])
                u.delete()
                return HttpResponseRedirect('/thanks/')
            else:
                u = Usuario.objects.get(nombre=form.cleaned_data['nombreAnterior'])
                u.nombre = form.cleaned_data['nombre']
                u.save()
                return HttpResponseRedirect('/thanks/')
    else:
        form = EditarUsuarioForm()

    return render(request,'Clientes/Editar.html',{'form':form})



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