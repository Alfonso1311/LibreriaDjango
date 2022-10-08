from django import forms
<<<<<<< Updated upstream
from .models import Directivo, Profesor
=======
from .models import Directivo, Profesor, Alumno, Grupo
>>>>>>> Stashed changes

class DirectivoForm(forms.ModelForm):
    class Meta:
        model = Directivo
        fields = '__all__'
        '''my_date_field = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2020)))'''

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = '__all__'
<<<<<<< Updated upstream
=======

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'  #['Nombre','Apellido,'Foto'] si quiero especificar campos de la base de datos 
        
class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = '__all__'  #['Nombre','Apellido,'Foto'] si quiero especificar campos de la base de datos 
        
>>>>>>> Stashed changes
