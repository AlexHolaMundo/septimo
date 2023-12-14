from django.shortcuts import render, redirect
from .models import Pais, Gobierno, Cultura
# Create your views here.
def home(request):
    return render (request, 'inicio.html')
def pais(request):
    paisesBdd=Pais.objects.all()
    return render (request, 'paises.html', {'paises': paisesBdd})

def guardarPais (request):
    nombre=request.POST['nombre']
    anio_fundacion=request.POST['anio_fundacion']
    poblacion=request.POST['poblacion']
    moneda=request.POST['moneda']
    idioma=request.POST['idioma']
    nuevoPais=Pais.objects.create(nombre=nombre, anio_fundacion=anio_fundacion, poblacion=poblacion, moneda=moneda, idioma=idioma)
    return redirect  ('/pais')

def elimiarPais (request, id):
    paisEliminar=Pais.objects.get(id=id)
    paisEliminar.delete()
    return redirect ('/pais/')

def gobierno(request):
    gobiernosBdd=Gobierno.objects.all()
    return render (request, 'gobierno.html', {'gobiernos': gobiernosBdd})

def guardarGobierno (request):
    tipo_gobierno=request.POST['tipo_gobierno']
    presidente=request.POST['presidente']
    forma_juridica=request.POST['forma_juridica']
    sistema_politico=request.POST['sistema_politico']
    deuda_externa=request.POST['deuda_externa']
    nuevoGobierno=Gobierno.objects.create(tipo_gobierno=tipo_gobierno, presidente=presidente, forma_juridica=forma_juridica, sistema_politico=sistema_politico, deuda_externa=deuda_externa)
    return redirect ('/gobierno')

def eliminarGobierno(request, id):
    gobiernoEliminar=Gobierno.objects.get(id=id)
    gobiernoEliminar.delete()
    return redirect (gobierno)

def cultura(request):
    culturasBdd=Cultura.objects.all()
    return render (request, 'cultura.html', {'culturas': culturasBdd})

def guardarCultura(request):
    nombre=request.POST['nombre']
    descripcion=request.POST['descripcion']
    religion=request.POST['religion']
    gastronomia=request.POST['gastronomia']
    musica=request.POST['musica']
    nuevaCultura=Cultura.objects.create(nombre=nombre, descripcion=descripcion, religion=religion, gastronomia=gastronomia, musica=musica)
    return redirect ('/cultura')

def eliminarCultura(request, id):
    culturaEliminar=Cultura.objects.get(id=id)
    culturaEliminar.delete()
    return redirect(cultura)