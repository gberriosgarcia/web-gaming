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