from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [

    path('login/', LoginView.as_view(template_name="registration/login.html"),name="login"),
    path('logout/', LogoutView.as_view(template_name="paginas/inicio.html"),name="salir"),
    
    path('', views.inicio, name='inicio'), # El nombre es para acceder a una url con ese nombre
    path('directivo', login_required(views.inicioD), name='inicioD'),
    path('profesor', login_required(views.inicioP), name='inicioP'),

    #path('login/', views.salir, name='salir'),

    path('directivos', login_required(views.directivos), name='directivos'),
    path('directivo/crear', login_required(views.crearDirectivo), name='crear'),
    path('directivo/editar/<str:id>', login_required(views.editarDirectivo), name='editar'),
    path('eliminar/<str:id>', login_required(views.eliminarDirectivo), name='eliminar'),

    path('profesores', login_required(views.profesores), name='profesores'),
    path('profesor/crear', login_required(views.crearProfesor), name='crearP'),
    path('profesor/editar/<str:id>', login_required(views.editarProfesor), name='editarP'),
    path('eliminarP/<str:id>', login_required(views.eliminarProfesor), name='eliminarP'),

    path('alumnos', login_required(views.alumnos), name='alumnos'), 
    path('alumno/crear', login_required(views.crearAlumno), name='crearA'),
    path('alumno/editar/<str:matricula>', login_required(views.editarAlumno), name='editarA'),
    path('eliminarA/<str:matricula>', login_required(views.eliminarAlumno), name='eliminarA'),

    path('grupos', login_required(views.grupos), name='grupos'),
    path('grupo/crear', login_required(views.crearGrupo), name='crearG'),
    path('grupo/editar/<int:id>', login_required(views.editarGrupo), name='editarG'),
    path('eliminarG/<int:id>', login_required(views.eliminarGrupo), name='eliminarG'),

    path('horarios', login_required(views.horarios), name='horarios'),
    path('horario/crear', login_required(views.crearHorario), name='crearH'),
    path('horario/editar/<int:id>', login_required(views.editarHorario), name='editarH'),
    path('eliminarH/<int:id>', login_required(views.eliminarHorario), name='eliminarH'),

    path('asistencias', login_required(views.asistencias), name='asistencias'),
    path('asistencia/crear', login_required(views.crearAsistencia), name='crearAsis'),
    path('asistencia/editar/<int:id>', login_required(views.editarAsistencia), name='editarAsis'),
    path('eliminarAsis/<int:id>', login_required(views.eliminarAsistencia), name='eliminarAsis'),

    path('justificantes', login_required(views.justificantes), name='justificantes'), 
    path('justificante/crear', login_required(views.crearJustificante), name='crearJ'),
    path('justificante/editar/<int:id>', login_required(views.editarJustificante), name='editarJ'),
    path('eliminarJ/<int:id>', login_required(views.eliminarJustificante), name='eliminarJ'),

    path('usuarios', login_required(views.usuarios), name='usuarios'), 
    path('usuario/crear', views.crearUsuario, name='crearU'),
    path('usuario/editar/<int:id>', login_required(views.editarUsuario), name='editarU'),
    path('eliminarU/<int:id>', login_required(views.eliminarUsuario), name='eliminarU'),

    path('asignaturas', login_required(views.asignaturas), name='asignaturas'),
    path('asignatura/crear', login_required(views.crearAsignatura), name='crearAsig'),
    path('asignatura/editar/<str:clave>', login_required(views.editarAsignatura), name='editarAsig'),
    path('eliminarAsig/<str:clave>', login_required(views.eliminarAsignatura), name='eliminarAsig'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)