from django.db import models

# Create your models here.
class Cliente(models.Model):
    id=models.AutoField(primary_key=True)
    cedula=models.CharField(max_length=10)
    apellido=models.CharField(max_length=100)
    nombre=models.CharField(max_length=100)
    direccion=models.TextField(max_length=100)
    fechas_nacimiento=models.DateField()
    correo=models.EmailField()
    def __str__(self):
        fila="{0} => {1} => {2} => {3} => {4} => {5} => {6}"
        return fila.format(self.id,self.cedula,self.apellido,self.nombre,self.direccion,self.fechas_nacimiento,self.correo)