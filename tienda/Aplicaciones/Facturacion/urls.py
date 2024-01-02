from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('guardarCliente/',views.guardarCliente),
    path('eliminarCliente/<int:id>',views.eliminarCliente),
    path('editarCliente/<int:id>',views.editarCliente),
    path('procesarActualizacionCliente/',views.procesarActualizacionCliente),
]
