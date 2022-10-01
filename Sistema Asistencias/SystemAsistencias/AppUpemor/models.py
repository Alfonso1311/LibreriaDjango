from enum import auto
from tabnanny import verbose
from django.db import models
from datetime import datetime, date

# Create your models here.

class Directivo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    apellidoP = models.CharField(max_length=100, verbose_name='Apellido P')
    apellidoM = models.CharField(max_length=100, verbose_name='Apellido M')
    fechaNac = models.DateField(auto_now_add=False, auto_now=False, blank=True ,verbose_name='Fecha Nac (yyyy-mm-dd)', null=True)
    '''hora = models.DateField(auto_now_add=True, auto_now=False, blank=True ,verbose_name='Fecha Nac')'''
    correo = models.EmailField(verbose_name='Correo', null=True)
    area = models.CharField(max_length=100, verbose_name='Area', null=True)

    def __str__(self):
        fila = "Nombre: " + self.nombre + " - " + " Apellido P: " + self.apellidoP
        return fila

    def delete(self, using=None, keep_parents=False):
        super().delete()