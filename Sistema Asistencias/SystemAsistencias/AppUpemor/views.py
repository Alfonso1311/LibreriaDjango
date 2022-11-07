from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from .models import Directivo, Profesor, Alumno, Grupo, Horario, Asistencia, Justificante, Usuario, Asignatura
from .forms import DirectivoForm, ProfesorForm, AlumnoForm, GrupoForm, HorarioForm, AsistenciaForm, JustificanteForm, UsuarioForm, AsignaturaForm
# Create your views here.

def salir(request):
    logout(request)
    return redirect('login/')

def inicio(request):
    return render(request, 'paginas/inicio.html')

def inicioD(request):
    return render(request, 'usuarios/directivo/inicioD.html')

def inicioP(request):
    return render(request, 'usuarios/profesor/inicioP.html')

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

def alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'usuarios/alumno/indexA.html', {'alumnos': alumnos})

def crearAlumno(request):
    formulario = AlumnoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('alumnos')
    return render(request, 'usuarios/alumno/crear.html', {'formulario': formulario})

def editarAlumno(request, matricula):
    alumno = Alumno.objects.get(matricula=matricula)
    formulario = AlumnoForm(request.POST or None, request.FILES or None, instance=alumno)
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

def horarios(request):
    horarios = Horario.objects.all()
    return render(request, 'horarios/indexH.html', {'horarios': horarios})

def crearHorario(request): 
    formulario = HorarioForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('horarios')
    return render(request, 'horarios/crear.html', {'formulario': formulario})

def editarHorario(request, id):
    horario = Horario.objects.get(id=id)
    formulario = HorarioForm(request.POST or None, instance=horario)
    if formulario.is_valid():
        formulario.save()
        return redirect('horarios')
    return render(request, 'horarios/editar.html', {'formulario': formulario, 'horario': horario})

def eliminarHorario(request, id):
    horario = Horario.objects.get(id=id)
    horario.delete()
    return redirect('horarios')

def asistencias(request):
    asistencias = Asistencia.objects.all()
    return render(request, 'asistencias/indexAsis.html', {'asistencias': asistencias})

def crearAsistencia(request): 
    formulario = AsistenciaForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('asistencias')
    return render(request, 'asistencias/crear.html', {'formulario': formulario})

def editarAsistencia(request, id):
    asistencia = Asistencia.objects.get(id=id)
    formulario = AsistenciaForm(request.POST or None, instance=asistencia)
    if formulario.is_valid():
        formulario.save()
        return redirect('asistencias')
    return render(request, 'asistencias/editar.html', {'formulario': formulario, 'asistencia': asistencia})

def eliminarAsistencia(request, id):
    asistencia = Asistencia.objects.get(id=id)
    asistencia.delete()
    return redirect('asistencias')

def justificantes(request):
    justificantes = Justificante.objects.all()
    return render(request, 'justificantes/indexJ.html', {'justificantes': justificantes})

def crearJustificante(request):
    formulario = JustificanteForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('justificantes')
    return render(request, 'justificantes/crear.html', {'formulario': formulario})

def editarJustificante(request, id):
    justificante = Justificante.objects.get(id=id)
    formulario = JustificanteForm(request.POST or None, request.FILES or None, instance=justificante)
    if formulario.is_valid():
        formulario.save()
        return redirect('justificantes')
    return render(request, 'justificantes/editar.html', {'formulario': formulario, 'justificante': justificante})

def eliminarJustificante(request, id):
    justificante = Justificante.objects.get(id=id)
    justificante.delete()
    return redirect('justificantes')

def usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'usuarios/usuario/indexU.html', {'usuarios': usuarios})

def crearUsuario(request):
    if request.method == 'POST':
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid():
            username = formulario.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado correctamente')
            formulario.save()
            return redirect('usuarios')
    else:
        formulario = UsuarioForm()
    return render(request, 'usuarios/usuario/crear.html', {'formulario': formulario})

def editarUsuario(request, id):
    usuario = User.objects.get(id=id)
    formulario = UsuarioForm(request.POST or None, instance=usuario)
    if formulario.is_valid():
        username = formulario.cleaned_data['username']
        messages.success(request, f'Usuario {username} modificado correctamente')
        formulario.save()
        return redirect('usuarios')
    return render(request, 'usuarios/usuario/editar.html', {'formulario': formulario, 'usuario': usuario})

def eliminarUsuario(request, id):
    usuario = User.objects.get(id=id)
    usuario.delete()
    return redirect('usuarios')
'''
class SignUpView(CreateView):
    model = Usuario
    form_class = SignUpForm

    def form_valid(self, form):
        
        #En este parte, si el formulario es valido guardamos lo que se obtiene de él y usamos authenticate para que el usuario incie sesión luego de haberse registrado y lo redirigimos al index
        
        form.save()
        usuario = form.cleaned_data.get('nomUsuario')
        password = form.cleaned_data.get('password')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('/')

class BienvenidaView(TemplateView):
   template_name = 'usuarios/directivo/inicioD.html'
'''
def asignaturas(request):
    asignaturas = Asignatura.objects.all()
    return render(request, 'asignaturas/indexAsig.html', {'asignaturas': asignaturas})

def crearAsignatura(request):
    formulario = AsignaturaForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('asignaturas')
    return render(request, 'asignaturas/crear.html', {'formulario': formulario})

def editarAsignatura(request, clave):
    asignatura = Asignatura.objects.get(clave=clave)
    formulario = AsignaturaForm(request.POST or None, instance=asignatura)
    if formulario.is_valid():
        formulario.save()
        return redirect('asignaturas')
    return render(request, 'asignaturas/editar.html', {'formulario': formulario, 'asignatura': asignatura})

def eliminarAsignatura(request, clave):
    asignatura = Asignatura.objects.get(clave=clave)
    asignatura.delete()
    return redirect('asignaturas')