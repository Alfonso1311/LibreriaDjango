from django.shortcuts import render, redirect
from django.http import HttpResponse
<<<<<<< Updated upstream
from .models import Directivo, Profesor
from .forms import DirectivoForm, ProfesorForm
=======
from .models import Directivo, Profesor, Alumno, Grupo
from .forms import DirectivoForm, ProfesorForm, AlumnoForm, GrupoForm
>>>>>>> Stashed changes
# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicioD.html')

def directivos(request):
    directivos = Directivo.objects.all()
    return render(request, 'usuarios/directivo/indexD.html', {'directivos': directivos})

def crearDirectivo(request):
    formulario = DirectivoForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('directivos')
    return render(request, 'usuarios/directivo/crear.html', {'formulario': formulario})

def editarDirectivo(request, id):
    directivo = Directivo.objects.get(id=id)
    formulario = DirectivoForm(request.POST or None, instance=directivo)
    if formulario.is_valid():
        formulario.save()
        return redirect('directivos')
    return render(request, 'usuarios/directivo/editar.html', {'formulario': formulario, 'directivo': directivo})

def eliminarDirectivo(request, id):
    directivo = Directivo.objects.get(id=id)
    directivo.delete()
    return redirect('directivos')

def profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'usuarios/profesor/indexP.html', {'profesores': profesores})

def crearProfesor(request):
    formulario = ProfesorForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('profesores')
    return render(request, 'usuarios/profesor/crear.html', {'formulario': formulario})

def editarProfesor(request, id):
    profesor = Profesor.objects.get(id=id)
    formulario = ProfesorForm(request.POST or None, instance=profesor)
    if formulario.is_valid():
        formulario.save()
        return redirect('profesores')
    return render(request, 'usuarios/profesor/editar.html', {'formulario': formulario, 'profesor': profesor})

def eliminarProfesor(request, id):
    profesor = Profesor.objects.get(id=id)
    profesor.delete()
<<<<<<< Updated upstream
    return redirect('profesores')
=======
    return redirect('profesores')

def alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'usuarios/alumno/indexA.html', {'alumnos': alumnos})

def crearAlumno(request):
    formulario = AlumnoForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('alumnos')
    return render(request, 'usuarios/alumno/crear.html', {'formulario': formulario})

def editarAlumno(request, matricula):
    alumno = Alumno.objects.get(matricula=matricula)
    formulario = AlumnoForm(request.POST or None, instance=alumno)
    if formulario.is_valid():
        formulario.save()
        return redirect('alumnos')
    return render(request, 'usuarios/alumno/editar.html', {'formulario': formulario, 'alumno': alumno})

def eliminarAlumno(request, matricula):
    alumno = Alumno.objects.get(matricula=matricula)
    alumno.delete()
    return redirect('alumnos')

def grupos(request):
    grupos = Grupo.objects.all()
    return render(request, 'grupos/indexG.html', {'grupos': grupos})

def crearGrupo(request):
    formulario = GrupoForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('grupos')
    return render(request, 'grupos/crear.html', {'formulario': formulario})

def editarGrupo(request, id):
    grupo = Grupo.objects.get(id=id)
    formulario = GrupoForm(request.POST or None, instance=grupo)
    if formulario.is_valid():
        formulario.save()
        return redirect('grupos')
    return render(request, 'grupos/editar.html', {'formulario': formulario, 'grupo': grupo})

def eliminarGrupo(request, id):
    grupo = Grupo.objects.get(id=id)
    grupo.delete()
    return redirect('grupos')

    
>>>>>>> Stashed changes
