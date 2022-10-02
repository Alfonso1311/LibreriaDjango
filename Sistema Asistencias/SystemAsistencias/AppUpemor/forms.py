from django import forms
from .models import Directivo, Profesor

class DirectivoForm(forms.ModelForm):
    class Meta:
        model = Directivo
        fields = '__all__'
        '''my_date_field = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2020)))'''

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = '__all__'
