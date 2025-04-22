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

# @login_required(login_url='login')
def supervivencia(request):
    return render(request, 'categorias/supervivencia.html')

# @login_required(login_url='login')
def deportes(request):
    return render(request, 'categorias/deportes.html')

# @login_required(login_url='login')
def accion(request):
    return render(request, 'categorias/accion.html')

# @login_required(login_url='login')
def mundo_abierto(request):
    return render(request, 'categorias/mundo_abierto.html')

# @login_required(login_url='login')
def carreras(request):
    return render(request, 'categorias/carreras.html')

# @login_required(login_url='login')
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

# Juegos de accion

# @login_required(login_url='login')
def helldivers(request):
    return render(request, 'preview_juegos/preview_hd.html')

# @login_required(login_url='login')
def split_fiction(request):
    return render(request, 'preview_juegos/preview_sf.html')

# @login_required(login_url='login')
def elden_ring(request):
    return render(request, 'preview_juegos/preview_er.html')

# Juegos de mundo abierto

# @login_required(login_url='login')
def ark(request):
    return render(request, 'preview_juegos/preview_ark.html')

# @login_required(login_url='login')
def gta(request):
    return render(request, 'preview_juegos/preview_gta.html')

# @login_required(login_url='login')
def monster_hunter(request):
    return render(request, 'preview_juegos/preview_mh.html')

# Juegos de carreras

# @login_required(login_url='login')
def ndfs(request):
    return render(request, 'preview_juegos/preview_ndfs.html')

# @login_required(login_url='login')
def most_wanted(request):
    return render(request, 'preview_juegos/preview_nfsmw.html')

# @login_required(login_url='login')
def f124(request):
    return render(request, 'preview_juegos/preview_f21.html')

# Juegos de deportes

# @login_required(login_url='login')
def fifa(request):
    return render(request, 'preview_juegos/preview_futb.html')

# @login_required(login_url='login')
def captain_tsubasa(request):
    return render(request, 'preview_juegos/preview_tsubasa.html')

# @login_required(login_url='login')
def nba(request):
    return render(request, 'preview_juegos/preview_nba.html')


# Juegos de supervivencia

# @login_required(login_url='login')
def minecraft(request):
    return render(request, 'preview_juegos/preview_minecraft.html')

# @login_required(login_url='login')
def rust(request):
    return render(request, 'preview_juegos/preview_rust.html')

# @login_required(login_url='login')
def the_forest(request):
    return render(request, 'preview_juegos/preview_forest.html')