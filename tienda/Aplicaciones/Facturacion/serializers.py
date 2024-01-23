from rest_framework import serializers
from .models import Tipo, Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cliente
        fields='__all__'

class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tipo
        fields='__all__'
