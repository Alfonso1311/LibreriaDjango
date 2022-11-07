from django.contrib import admin
from .models import Directivo, Profesor, Alumno, Grupo, Horario, Asistencia, Justificante, Usuario, Asignatura

# Register your models here.
admin.site.register(Directivo)
admin.site.register(Profesor)
admin.site.register(Alumno)
admin.site.register(Grupo)
admin.site.register(Horario)
admin.site.register(Asistencia)
admin.site.register(Justificante)
admin.site.register(Usuario)
admin.site.register(Asignatura)