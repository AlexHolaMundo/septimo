from django.shortcuts import render
from .models import Cliente
# Create your views here.
def home(request):
    clientesBdd=Cliente.objects.all()
    return render (request, 'listadoClientes.html', {'clientes': clientesBdd})