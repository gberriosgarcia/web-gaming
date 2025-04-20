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
            return render(request, 'login.html', {'error': 'Credenciales incorrectas'})
    return render(request, 'login.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('index')

# @login_required(login_url='login')
def terror(request):
    return render(request, 'categorias/terror.html')

# @login_required(login_url='login')
def accion(request):
    return render(request, 'categorias/accion.html')

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

# Juegos de Accion

# @login_required(login_url='login')
def helldivers(request):
    return render(request, 'preview_juegos/preview_hd.html')

# @login_required(login_url='login')
def split_fiction(request):
    return render(request, 'preview_juegos/preview_sf.html')

# @login_required(login_url='login')
def elden_ring(request):
    return render(request, 'preview_juegos/preview_er.html')