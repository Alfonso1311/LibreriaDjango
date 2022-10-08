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
<<<<<<< Updated upstream
=======

    path('alumnos', views.alumnos, name='alumnos'),
    path('alumno/crear', views.crearAlumno, name='crearA'),
    path('alumno/editar/<str:matricula>', views.editarAlumno, name='editarA'),
    path('eliminarA/<str:matricula>', views.eliminarAlumno, name='eliminarA'),

    path('grupos', views.grupos, name='grupos'),
    path('grupo/crear', views.crearGrupo, name='crearG'),
    path('grupo/editar/<int:id>', views.editarGrupo, name='editarG'),
    path('eliminarG/<int:id>', views.eliminarGrupo, name='eliminarG'),
>>>>>>> Stashed changes
]