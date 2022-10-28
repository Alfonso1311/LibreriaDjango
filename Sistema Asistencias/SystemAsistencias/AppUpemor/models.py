from asyncio.windows_events import NULL
from distutils.command import upload
from enum import auto
from pickle import TRUE
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import datetime, date

# Create your models here.

class Directivo(models.Model):
    id = models.CharField(primary_key=True, max_length=15, verbose_name='ID_Directivo')
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    apellidoP = models.CharField(max_length=100, verbose_name='Apellido P')
    apellidoM = models.CharField(max_length=100, verbose_name='Apellido M', null=True)
    fechaNac = models.DateField(auto_now_add=False, auto_now=False, blank=True ,verbose_name='Fecha Nac (yyyy-mm-dd)', null=True)
    correo = models.EmailField(verbose_name='Correo', null=True)
    area = models.CharField(max_length=100, verbose_name='Area')

    def __str__(self):
        fila = "Nombre: " + self.nombre + " - " + " Apellido P: " + self.apellidoP
        return fila

    def delete(self, using=None, keep_parents=False):
        super().delete()

class Profesor(models.Model):
    id = models.CharField(primary_key=True, max_length=15, verbose_name='ID_Profesor')
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    apellidoP = models.CharField(max_length=100, verbose_name='Apellido P')
    apellidoM = models.CharField(max_length=100, verbose_name='Apellido M', null=True)
    fechaNac = models.DateField(auto_now_add=False, auto_now=False, blank=True ,verbose_name='Fecha Nac (yyyy-mm-dd)', null=True)
    correo = models.EmailField(verbose_name='Correo', null=True)
    da = models.CharField(max_length=100, verbose_name='DA', null=True)

    def __str__(self):
        fila = "Nombre: " + self.nombre + " - " + " Apellido P: " + self.apellidoP
        return fila

    def delete(self, using=None, keep_parents=False):
        super().delete()

class Alumno(models.Model):
    matricula = models.CharField(max_length=15, primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    apellidoP = models.CharField(max_length=100, verbose_name='Apellido P')
    apellidoM = models.CharField(max_length=100, verbose_name='Apellido M', null=True)
    fechaNac = models.DateField(auto_now_add=False, auto_now=False, blank=True ,verbose_name='Fecha Nac (yyyy-mm-dd)', null=True)
    correo = models.EmailField(verbose_name='Correo', null=True)
    imagen = models.ImageField(upload_to='imagenes/', verbose_name='Imagen', null=True)
    grupo = models.CharField(max_length=10, verbose_name='Grupo_ID')

    def __str__(self):
        fila = "Nombre: " + self.nombre + " - " + " Apellido P: " + self.apellidoP
        return fila

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

class Grupo(models.Model):
    id = models.AutoField(primary_key=True)
    cuatri = models.IntegerField(verbose_name='Cuatrimestre')
    grupo = models.CharField(max_length=100, verbose_name='Grupo')
    carrera = models.CharField(max_length=100, verbose_name='Carrera')

    def delete(self, using=None, keep_parents=False):
        super().delete()

class Horario(models.Model):
    id = models.AutoField( primary_key=True)
    horaEntrada = models.TimeField(auto_now=True, verbose_name='Hora de entrada')
    tolerancia = models.IntegerField(verbose_name='Tolerancia', null=True)

    def delete(self, using=None, keep_parents=False):
        super().delete()

class Asistencia(models.Model):
    id = models.AutoField(primary_key=True)
    grupo = models.CharField(max_length=100, verbose_name='Grupo')
    status = models.CharField(max_length=100, verbose_name='Status', null=True)
    fechaReg = models.DateField(auto_now_add=False, auto_now=False, blank=True ,verbose_name='Fecha Reg (yyyy-mm-dd)', null=True)
    matricula = models.CharField(max_length=100, verbose_name='Matricula_Alumno', null=True)

    def delete(self, using=None, keep_parents=False):
        super().delete()

class Justificante(models.Model):
    id = models.AutoField(primary_key=True)
    fechaJusti = models.DateField(auto_now_add=False, auto_now=False, blank=True ,verbose_name='Fecha de justificante (yyyy-mm-dd)', null=True)
    motivo = models.CharField(max_length=100, verbose_name='motivo')
    receta = models.FileField(upload_to='archivos/', verbose_name='archivo', null=True)
    matricula = models.CharField(max_length=100, verbose_name='Matricula_Alumno', null=True)
    
    def __str__(self):
        fila = "Nombre: " + self.nombre + " - " + " Apellido P: " + self.apellidoP
        return fila

    def delete(self, using=None, keep_parents=False):
        super().delete()

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nomUsuario = models.CharField(max_length=100, verbose_name='Nombre de Usuario')
    password = models.CharField(max_length=100, verbose_name='Password')
    directivo_id = models.CharField(max_length=15, verbose_name='ID_Directivo')
    profesor_id = models.CharField(max_length=15, verbose_name='ID_Profesor')
    alumno_matricula = models.CharField(max_length=15, verbose_name='Matricula_Alumno')
    
    def __str__(self):
        fila = "Nombre: " + self.nombre + " - " + " Apellido P: " + self.apellidoP
        return fila

    def delete(self, using=None, keep_parents=False):
        super().delete()

class Asignatura(models.Model):
    clave = models.CharField(max_length=100, verbose_name='Clave')
    nomAsignatura = models.CharField(max_length=100, verbose_name='Nombre de Asignatura')
    horario_id = models.IntegerField(verbose_name='ID_Horario')
    profesor_id = models.CharField(max_length=15, verbose_name='ID_Profesor')
    grupo_id = models.IntegerField(verbose_name='ID_Grupo')
    
    def __str__(self):
        fila = "Nombre: " + self.nombre + " - " + " Apellido P: " + self.apellidoP
        return fila

    def delete(self, using=None, keep_parents=False):
        super().delete()
