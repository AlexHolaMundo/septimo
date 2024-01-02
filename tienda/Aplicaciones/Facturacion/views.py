from django.shortcuts import render, redirect
from .models import Cliente
from django.contrib import messages
# Create your views here.
def home(request):
    clientesBdd=Cliente.objects.all()
    return render (request, 'listadoClientes.html', {'clientes': clientesBdd})

def guardarCliente (request):
    cedula=request.POST['cedula']
    nombre=request.POST['nombre']
    apellido=request.POST['apellido']
    fechas_nacimiento=request.POST['fechas_nacimiento']
    correo=request.POST['correo']
    direccion=request.POST['direccion']
    nuevoCliente=Cliente.objects.create(cedula=cedula, nombre=nombre, apellido=apellido, fechas_nacimiento=fechas_nacimiento, correo=correo, direccion=direccion)
    messages.success(request, 'Cliente guardado correctamente')
    return redirect  ('/')

def eliminarCliente (request, id):
    clienteEliminar=Cliente.objects.get(id=id)
    clienteEliminar.delete()
    messages.success(request, 'Cliente eliminado correctamente')
    return redirect ('/')

def editarCliente (request, id):
    clienteEditar=Cliente.objects.get(id=id)
    return render (request, 'editarCliente.html', {'cliente': clienteEditar})

def procesarActualizacionCliente (request):
    id=request.POST['id']
    cedula=request.POST['cedula']
    nombre=request.POST['nombre']
    apellido=request.POST['apellido']
    fechas_nacimiento=request.POST['fechas_nacimiento']
    correo=request.POST['correo']
    direccion=request.POST['direccion']
    cliente=Cliente.objects.get(id=id)
    cliente.cedula=cedula
    cliente.nombre=nombre
    cliente.apellido=apellido
    cliente.fechas_nacimiento=fechas_nacimiento
    cliente.correo=correo
    cliente.direccion=direccion
    cliente.save()
    messages.success(request, 'Cliente actualizado correctamente')
    return redirect ('/')