from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.
# @login_required(login_url='login')
def index(request):
    return render(request, 'index.html')

# @login_required(login_url='login')
def categorias(request):
    return render(request, 'menu/categorias.html')

# @login_required(login_url='login')
def registro(request):
    return render(request, 'menu/registro.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/') 
        else:
            return render(request, 'menu/login.html', {'error': 'Credenciales incorrectas'})
    return render(request, 'menu/login.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('index')

# @login_required(login_url='login')
def terror(request):
    return render(request, 'categorias/terror.html')

def supervivencia(request):
    return render(request, 'categorias/supervivencia.html')

def deportes(request):
    return render(request, 'categorias/deportes.html')

def accion(request):
    return render(request, 'categorias/accion.html')

def mundo_abierto(request):
    return render(request, 'categorias/mundo_abierto.html')

def carreras(request):
    return render(request, 'categorias/carreras.html')

def reinicio_pass(request):
    return render(request, 'menu/reinicio_pass.html')



# Juegos de Terror

# @login_required(login_url='login')
def resident_evil_village(request):
    return render(request, 'preview_juegos/preview_rv.html')

# @login_required(login_url='login')
def outlast(request):
    return render(request, 'preview_juegos/preview_ol.html')

# @login_required(login_url='login')
def resident_evil(request):
    return render(request, 'preview_juegos/preview_rev6.html')


def helldivers(request):
    return render(request, 'preview_juegos/preview_hd.html')

def split_fiction(request):
    return render(request, 'preview_juegos/preview_sf.html')

def elden_ring(request):
    return render(request, 'preview_juegos/preview_er.html')

#juegos de mundo abrido xd
def ark(request):
    return render(request, 'preview_juegos/preview_ark.html')

def gta(request):
    return render(request, 'preview_juegos/preview_gta.html')

def monster_hunter(request):
    return render(request, 'preview_juegos/preview_mh.html')

#juegos de carreas
def ndfs(request):
    return render(request, 'preview_juegos/preview_ndfs.html')

def most_wanted(request):
    return render(request, 'preview_juegos/preview_nfsmw.html')

def f124(request):
    return render(request, 'preview_juegos/preview_f21.html')