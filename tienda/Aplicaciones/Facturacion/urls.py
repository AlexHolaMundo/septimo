from django.urls import path
from . import views
from rest_framework import routers
from .api import TipoViewSet, ClienteViewSet

router = routers.DefaultRouter()
router.register('api/clientes',ClienteViewSet,'clientes')
router.register('api/tipos',TipoViewSet,'tipos')

urlpatterns = [
    path('',views.home),
    path('guardarCliente/',views.guardarCliente),
    path('eliminarCliente/<int:id>',views.eliminarCliente),
    path('editarCliente/<int:id>',views.editarCliente),
    path('procesarActualizacionCliente/',views.procesarActualizacionCliente),
]

urlpatterns += router.urls
