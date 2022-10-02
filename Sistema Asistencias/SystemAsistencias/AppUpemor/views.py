from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Directivo, Profesor
from .forms import DirectivoForm, ProfesorForm
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
    return redirect('profesores')