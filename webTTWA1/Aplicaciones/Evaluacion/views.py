from django.shortcuts import render
from .models import Pais, Gobierno, Cultura
# Create your views here.
def home(request):
    return render (request, 'inicio.html')
def pais(request):
    paisesBdd=Pais.objects.all()
    return render (request, 'paises.html', {'paises': paisesBdd})

def gobierno(request):
    gobiernosBdd=Gobierno.objects.all()
    return render (request, 'gobierno.html', {'gobiernos': gobiernosBdd})

def cultura(request):
    culturasBdd=Cultura.objects.all()
    return render (request, 'cultura.html', {'culturas': culturasBdd})