from django.shortcuts import render
from django.template import RequestContext
from proyecto1.models import Usuario
from django.shortcuts import  render_to_response
from django.http import HttpResponseRedirect
# Create your views here.

from .forms import UsuarioForm
from .forms import EditarUsuarioForm
from django import forms

def index(request):
    return render(request,'Index.html')

def indexClientes(request):
    return  render(request,'Clientes/Index.html')

def insertarClientes(request):
    if request.method =='POST':
        form = UsuarioForm(request.POST)

        if form.is_valid():
            u = Usuario(nombre=form.cleaned_data['nombre'])
            u.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = UsuarioForm()

    return render(request,'Clientes/Insertar.html',{'form':form})

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