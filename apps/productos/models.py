from django.db import models

# Create your models here.
class producto(models.Model):
    nombre = models.CharField(max_length=100, default='')
    descripcion = models.CharField(max_length=200, default='')
    estatus = models.ForeignKey('estatu', blank=True, null=True)
    marcas = models.ForeignKey('marca', blank=True, null=True)

    def __str__(self):
        return self.nombre

class estatu(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre

class marca(models.Model):
    nombre = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nombre
