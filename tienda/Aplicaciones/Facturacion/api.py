from .models import Tipo, Cliente
from rest_framework import viewsets, permissions
from .serializers import TipoSerializer, ClienteSerializer

class TipoViewSet(viewsets.ModelViewSet):
    queryset=Tipo.objects.all()
    permission_classes=[
        permissions.AllowAny
    ]
    serializer_class=TipoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset=Cliente.objects.all()
    permission_classes=[
        permissions.AllowAny
    ]
    serializer_class=ClienteSerializer
