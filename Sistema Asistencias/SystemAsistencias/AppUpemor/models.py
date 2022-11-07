from asyncio.windows_events import NULL
from distutils.command import upload
from enum import auto
from pickle import TRUE
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime, date

from django.db.models.signals import post_save

# Create your models here.

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Directivo.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)

class Directivo(models.Model):
    #id = models.CharField(primary_key=True, max_length=15, verbose_name='ID_Directivo')
    id = models.AutoField(primary_key=True, verbose_name='ID_Directivo')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='directivo')
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    apellidoP = models.CharField(max_length=100, verbose_name='Apellido P')
    apellidoM = models.CharField(max_length=100, verbose_name='Apellido M', null=True, blank=True, default='')
    fechaNac = models.DateField(auto_now_add=False, auto_now=False, blank=True ,verbose_name='Fecha Nac (yyyy-mm-dd)', default=timezone.now)
    correo = models.EmailField(verbose_name='Correo', null=True, blank=True, default='')
    area = models.CharField(max_length=100, verbose_name='Area')
    userType = models.CharField(max_length=100, verbose_name='', default='Directivo')
    

    def __str__(self):
        fila = f'{self.user.username} - {self.nombre} {self.apellidoP}'
        return fila

    def delete(self, using=None, keep_parents=False):
        super().delete()

class Profesor(models.Model):
    id = models.CharField(primary_key=True, max_length=15, verbose_name='ID_Profesor')
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    apellidoP = models.CharField(max_length=100, verbose_name='Apellido P')
    apellidoM = models.CharField(max_length=100, verbose_name='Apellido M', null=True)
    fechaNac = models.DateField(auto_now_add=False, auto_now=False, blank=True ,verbose_name='Fecha Nac (yyyy-mm-dd)', default=timezone.now)
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
    fechaNac = models.DateField(auto_now_add=False, auto_now=False, blank=True ,verbose_name='Fecha Nac (yyyy-mm-dd)', default=timezone.now)
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
    fechaReg = models.DateField(auto_now_add=False, auto_now=False, blank=True ,verbose_name='Fecha Reg (yyyy-mm-dd)', default=timezone.now)
    matricula = models.CharField(max_length=100, verbose_name='Matricula_Alumno', null=True)

    def delete(self, using=None, keep_parents=False):
        super().delete()

class Justificante(models.Model):
    id = models.AutoField(primary_key=True)
    fechaJusti = models.DateField(auto_now_add=False, auto_now=False, blank=True ,verbose_name='Fecha de justificante (yyyy-mm-dd)', default=timezone.now)
    motivo = models.CharField(max_length=100, verbose_name='motivo')
    receta = models.FileField(upload_to='archivos/', verbose_name='archivo', null=True)
    matricula = models.CharField(max_length=100, verbose_name='Matricula_Alumno', null=True)
    
    def __str__(self):
        fila = "Nombre: " + self.nombre + " - " + " Apellido P: " + self.apellidoP
        return fila

    def delete(self, using=None, keep_parents=False):
        super().delete()
'''
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
'''
class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, default=1)
    userType = models.CharField(max_length=100, verbose_name='', default='No')
    image = models.ImageField(upload_to='user_profile/', verbose_name='Imagen', null=True)


    #user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario')

    def __str__(self):
        return f'Perfil de {self.user.username}'

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
