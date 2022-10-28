from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    
    path('', views.inicio, name='inicio'), # El nombre es para acceder a una url con ese nombre
    path('directivos', views.directivos, name='directivos'),
    path('directivo/crear', views.crearDirectivo, name='crear'),
    path('directivo/editar/<int:id>', views.editarDirectivo, name='editar'),
    path('eliminar/<int:id>', views.eliminarDirectivo, name='eliminar'),

    path('profesores', views.profesores, name='profesores'),
    path('profesor/crear', views.crearProfesor, name='crearP'),
    path('profesor/editar/<int:id>', views.editarProfesor, name='editarP'),
    path('eliminarP/<int:id>', views.eliminarProfesor, name='eliminarP'),

    path('alumnos', views.alumnos, name='alumnos'), 
    path('alumno/crear', views.crearAlumno, name='crearA'),
    path('alumno/editar/<str:matricula>', views.editarAlumno, name='editarA'),
    path('eliminarA/<str:matricula>', views.eliminarAlumno, name='eliminarA'),

    path('grupos', views.grupos, name='grupos'),
    path('grupo/crear', views.crearGrupo, name='crearG'),
    path('grupo/editar/<int:id>', views.editarGrupo, name='editarG'),
    path('eliminarG/<int:id>', views.eliminarGrupo, name='eliminarG'),

    path('horarios', views.horarios, name='horarios'),
    path('horario/crear', views.crearHorario, name='crearH'),
    path('horario/editar/<int:id>', views.editarHorario, name='editarH'),
    path('eliminarH/<int:id>', views.eliminarHorario, name='eliminarH'),

    path('asistencias', views.asistencias, name='asistencias'),
    path('asistencia/crear', views.crearAsistencia, name='crearAsis'),
    path('asistencia/editar/<int:id>', views.editarAsistencia, name='editarAsis'),
    path('eliminarAsis/<int:id>', views.eliminarAsistencia, name='eliminarAsis'),

    path('justificantes', views.justificantes, name='justificantes'), 
    path('justificante/crear', views.crearJustificante, name='crearJ'),
    path('justificante/editar/<int:id>', views.editarJustificante, name='editarJ'),
    path('eliminarJ/<int:id>', views.eliminarJustificante, name='eliminarJ'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)