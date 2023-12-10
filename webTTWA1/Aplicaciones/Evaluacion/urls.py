from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('pais/',views.pais, name='pais'),
    path('gobierno/',views.gobierno, name='gobierno'),
    path('cultura/', views.cultura, name='cultura'),
]