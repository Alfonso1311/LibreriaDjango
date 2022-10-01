from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Directivo
from .forms import DirectivoForm
# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicioD.html')

def directivos(request):
    directivos = Directivo.objects.all()
    return render(request, 'usuarios/directivo/index.html', {'directivos': directivos})

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