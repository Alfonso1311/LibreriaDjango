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

class Profesor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    apellidoP = models.CharField(max_length=100, verbose_name='Apellido P')
    apellidoM = models.CharField(max_length=100, verbose_name='Apellido M')
    fechaNac = models.DateField(auto_now_add=False, auto_now=False, blank=True ,verbose_name='Fecha Nac (yyyy-mm-dd)', null=True)
    correo = models.EmailField(verbose_name='Correo', null=True)
    da = models.CharField(max_length=100, verbose_name='DA', null=True)

    def __str__(self):
        fila = "Nombre: " + self.nombre + " - " + " Apellido P: " + self.apellidoP
        return fila

    def delete(self, using=None, keep_parents=False):
<<<<<<< Updated upstream
=======
        super().delete()

class Alumno(models.Model):
    matricula = models.CharField(max_length=15, primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    apellidoP = models.CharField(max_length=100, verbose_name='Apellido P')
    apellidoM = models.CharField(max_length=100, verbose_name='Apellido M')
    fechaNac = models.DateField(auto_now_add=False, auto_now=False, blank=True ,verbose_name='Fecha Nac (yyyy-mm-dd)', null=True)
    correo = models.EmailField(verbose_name='Correo', null=True)
    carrera = models.CharField(max_length=100, verbose_name='Carrera')
    cuatri = models.IntegerField(verbose_name='Cuatrimestre')
    grupo = models.CharField(max_length=10, verbose_name='Grupo')
    #foto = models.ImageField(upload_to='imagenes/', verbose_name='Imagen', null=True)

    def __str__(self):
        fila = "Nombre: " + self.nombre + " - " + " Apellido P: " + self.apellidoP
        return fila

    def delete(self, using=None, keep_parents=False):
        super().delete()

class Grupo(models.Model):
    id = models.AutoField(max_length=15, primary_key=True)
    cuatri = models.IntegerField(max_length=100, verbose_name='Cuatrimestre')
    grupo = models.CharField(max_length=100, verbose_name='Grupo')
    asignatura = models.CharField(max_length=100, verbose_name='Asignatura')
    profesor = models.CharField(max_length=100, verbose_name='Profesor')
    carrera = models.CharField(max_length=100, verbose_name='Carrera')

    def delete(self, using=None, keep_parents=False):
>>>>>>> Stashed changes
        super().delete()