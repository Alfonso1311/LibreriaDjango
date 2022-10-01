from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'), # Eel nombre es para acceder a una url con ese nombre
    path('directivos', views.directivos, name='directivos'),
    path('directivo/crear', views.crearDirectivo, name='crear'),
    path('directivo/editar/<int:id>', views.editarDirectivo, name='editar'),
   path('eliminar/<int:id>', views.eliminarDirectivo, name='eliminar'),
]