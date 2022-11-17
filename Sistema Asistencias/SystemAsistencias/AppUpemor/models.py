from asyncio.windows_events import NULL
from distutils.command import upload
from enum import auto
from pickle import TRUE
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models
from .choices import CARERS_CHOICES
from django.contrib.auth.models import User, AbstractUser
from django.utils import timezone
from datetime import datetime, date
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, Border, Side, PatternFill

from django.db.models.signals import post_save

# Create your models here.
'''
def create_user_profile(sender, instance, created, **kwargs):
    if created: #and instance.userType == "Directivo"
        Directivo.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
'''
class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, default=1, related_name='usuario')

    def __str__(self):
        return f'Perfil de {self.user.username}'

    def delete(self, using=None, keep_parents=False):
        super().delete()

class Directivo(models.Model):
    #id = models.CharField(primary_key=True, max_length=15, verbose_name='ID_Directivo')
    id = models.AutoField(primary_key=True, verbose_name='ID_Directivo')
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    apellidoP = models.CharField(max_length=100, verbose_name='Apellido P')
    apellidoM = models.CharField(max_length=100, verbose_name='Apellido M', null=True, blank=True, default='')
    fechaNac = models.DateField(auto_now_add=False, auto_now=False, blank=True ,verbose_name='Fecha Nac (yyyy-mm-dd)', default=timezone.now)
    correo = models.EmailField(verbose_name='Correo', null=True, blank=True, default='')
    area = models.CharField(max_length=100, verbose_name='Area')
    userType = models.CharField(max_length=100, verbose_name='', default='Directivo')
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='ID_Usuario', related_name='directivo')
    

    def __str__(self):
        fila = f'{self.user.username} - {self.nombre} {self.apellidoP}'
        return fila

    def delete(self, using=None, keep_parents=False):
        super().delete()

class Profesor(models.Model):
    id = models.CharField(primary_key=True, max_length=15, verbose_name='ID_Profesor')
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    apellidoP = models.CharField(max_length=100, verbose_name='Apellido P')
    apellidoM = models.CharField(max_length=100, verbose_name='Apellido M', null=True, blank=True)
    fechaNac = models.DateField(auto_now_add=False, auto_now=False, blank=True ,verbose_name='Fecha Nac (yyyy-mm-dd)', default=timezone.now)
    correo = models.EmailField(verbose_name='Correo', null=True)
    da = models.CharField(max_length=100, verbose_name='DA', null=True)
    userType = models.CharField(max_length=100, verbose_name='', default='Profesor')
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='ID_Usuario', related_name='profesorUser')

    def __str__(self):
        fila = "Nombre: " + self.nombre + " - " + " Apellido P: " + self.apellidoP
        return fila

    def delete(self, using=None, keep_parents=False):
        super().delete()

class Grupo(models.Model):

    id = models.AutoField(primary_key=True)
    cuatri = models.IntegerField(verbose_name='Cuatrimestre')
    grupo = models.CharField(max_length=1, verbose_name='Grupo')
    carrera = models.CharField(max_length=3, verbose_name='Carrera', default='')
    #alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, verbose_name='ID_Alumno', related_name='alumno', default='')

    def delete(self, using=None, keep_parents=False):
        super().delete()

class Alumno(models.Model):
    matricula = models.CharField(max_length=15, primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    apellidoP = models.CharField(max_length=100, verbose_name='Apellido P')
    apellidoM = models.CharField(max_length=100, verbose_name='Apellido M', null=True, blank=True)
    fechaNac = models.DateField(auto_now_add=False, auto_now=False, blank=True ,verbose_name='Fecha Nac (yyyy-mm-dd)', default=timezone.now)
    correo = models.EmailField(verbose_name='Correo', null=True)
    imagen = models.ImageField(upload_to='imagenes/', verbose_name='Imagen', null=True)
    userType = models.CharField(max_length=100, verbose_name='', default='Alumno')
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='ID_Usuario', related_name='alumnoUser')
    grupo_id = models.ForeignKey(Grupo, on_delete=models.CASCADE, verbose_name='ID_Grupo', related_name='grupoAlum', default='')
    
    #grupo = models.ModelChoiceField(queryset=Grupo.objects.order_by('id').values_list('carrera', flat=True).distinct(),empty_label=None, label=None, required=True)
    #grupo = models.CharField(max_length=10, verbose_name='Grupo_ID')

    def __str__(self):
        fila = self.nombre
        return fila

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

class Horario(models.Model):
    id = models.AutoField( primary_key=True)
    horaEntrada = models.TimeField(auto_now=True, verbose_name='Hora de entrada')
    tolerancia = models.IntegerField(verbose_name='Tolerancia', null=True, blank=True)

    def delete(self, using=None, keep_parents=False):
        super().delete()

class Asistencia(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=15, verbose_name='estatus', default='')
    fechaReg = models.DateField(auto_now_add=False, auto_now=False, blank=True ,verbose_name='Fecha Reg (yyyy-mm-dd)', default=timezone.now)
    id_alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, verbose_name='ID_Alumno', related_name='alumnoAsis', default='')

    def delete(self, using=None, keep_parents=False):
        super().delete()

class Justificante(models.Model):
    id = models.AutoField(primary_key=True)
    fechaJusti = models.DateField(auto_now_add=False, auto_now=False, blank=True ,verbose_name='Fecha de justificante (yyyy-mm-dd)', default=timezone.now)
    motivo = models.CharField(max_length=100, verbose_name='motivo')
    receta = models.FileField(upload_to='archivos/', verbose_name='archivo', null=True)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, verbose_name='ID_Alumno', related_name='alumnoJus', default='')
    
    def __str__(self):
        fila = "Nombre: " + self.nombre + " - " + " Apellido P: " + self.apellidoP
        return fila

    def delete(self, using=None, keep_parents=False):
        super().delete()

class Asignatura(models.Model):
    clave = models.CharField(max_length=100, verbose_name='Clave')
    nomAsignatura = models.CharField(max_length=100, verbose_name='Nombre de Asignatura')
    #horario_id = models.IntegerField(verbose_name='ID_Horario')
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE, verbose_name='ID_Horario', related_name='horarioAsig', default='')
    #profesor_id = models.CharField(max_length=15, verbose_name='ID_Profesor')
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, verbose_name='ID_Profesor', related_name='profesorAsig', default='')
    #grupo_id = models.IntegerField(verbose_name='ID_Grupo')
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, verbose_name='ID_Grupo', related_name='grupoAsig', default='')
    
    def __str__(self):
        fila = "Nombre: " + self.nombre + " - " + " Apellido P: " + self.apellidoP
        return fila

    def delete(self, using=None, keep_parents=False):
        super().delete()

