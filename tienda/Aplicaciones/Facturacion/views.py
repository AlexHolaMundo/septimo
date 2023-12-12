from django.shortcuts import render, redirect
from .models import Cliente
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
    return redirect  ('/')