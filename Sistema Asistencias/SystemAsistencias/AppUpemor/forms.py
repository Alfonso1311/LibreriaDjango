from dataclasses import fields
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Asistencia, Directivo, Profesor, Alumno, Grupo, Horario, Asistencia, Justificante, Usuario, Asignatura

class DirectivoForm(forms.ModelForm):
    class Meta:
        model = Directivo
        fields = '__all__'
        '''my_date_field = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2020)))'''

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = '__all__' 

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'  #['Nombre','Apellido,'Foto'] si quiero especificar campos de la base de datos 
        
class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = '__all__'
        
class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = '__all__'
        
class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = '__all__'
        
class JustificanteForm(forms.ModelForm):
    class Meta:
        model = Justificante
        fields = '__all__'

class UsuarioForm(UserCreationForm):
    password1: forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2: forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

'''
class SignUpView(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
'''

class AsignaturaForm(forms.ModelForm):
    class Meta:
        model = Asignatura
        fields = '__all__'