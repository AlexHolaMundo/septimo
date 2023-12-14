from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('pais/',views.pais, name='pais'),
    path('guardarPais/',views.guardarPais),
    path('eliminarPais/<int:id>',views.elimiarPais),
    path('gobierno/',views.gobierno, name='gobierno'),
    path('guardarGobierno/', views.guardarGobierno),
    path('eliminarGobierno/<int:id>', views.eliminarGobierno),
    path('cultura/', views.cultura, name='cultura'),
    path('guardarCultura/', views.guardarCultura),
    path('eliminarCultura/<int:id>', views.eliminarCultura),
]