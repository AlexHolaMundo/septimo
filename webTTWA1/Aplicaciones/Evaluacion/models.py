from django.db import models

# Create your models here.

class Pais (models.Model):
    id = models.AutoField(primary_key=True, verbose_name='Id del Pais')
    nombre = models.CharField(max_length=50, verbose_name='Nombre del Pais')
    anio_fundacion = models.DateField(verbose_name='Año de Fundación')
    poblacion = models.IntegerField(verbose_name='Población')
    moneda = models.CharField(max_length=50, verbose_name='Moneda')
    idioma = models.CharField(max_length=50, verbose_name='Idioma')

    def __str__(self):
        fila= "{0} {1} {2} {3} {4} {5}"
        return fila.format(self.id, self.nombre, self.anio_fundacion, self.poblacion, self.moneda, self.idioma)
class Gobierno(models.Model):
    id= models.AutoField(primary_key=True, verbose_name='Id del Gobierno')
    tipo_gobierno= models.CharField(max_length=50, verbose_name='Tipo de Gobierno')
    presidente= models.CharField(max_length=50, verbose_name='Presidente')
    forma_juridica= models.CharField(max_length=50, verbose_name='Capital')
    sistema_politico= models.CharField(max_length=50, verbose_name='Sistema Politico')
    deuda_externa= models.CharField(max_length=50, verbose_name='Deuda Externa')

    def __str__(self):
        fila= "{0} {1} {2} {3} {4} {5}"
        return fila.format(self.id, self.tipo_gobierno, self.presidente, self.forma_juridica, self.sistema_politico, self.deuda_externa)

class Cultura(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='Id de la Cultura')
    nombre = models.CharField(max_length=50, verbose_name='Nombre de la Cultura')
    descripcion = models.CharField(max_length=50, verbose_name='Descripcion')
    religion = models.CharField(max_length=50, verbose_name='Religion')
    gastronomia = models.CharField(max_length=50, verbose_name='Gastronomia')
    musica = models.CharField(max_length=50, verbose_name='Musica')

    def __str__(self):
        fila = "{0} {1} {2} {3} {4} {5}"
        return fila.format(self.id, self.nombre, self.descripcion, self.religion, self.gastronomia, self.musica)