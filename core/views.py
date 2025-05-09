from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as login_user, logout
from django.contrib.auth.models import User
from django.contrib import messages
from rest_api.models import Carrito, ItemCarrito, Juego

def index(request):
    return render(request, 'index.html')

@login_required(login_url='login')
def categorias(request):
    return render(request, 'menu/categorias.html')

def registro(request):
    if request.method == 'POST':
        nombre = request.POST.get('firstName')
        apellido = request.POST.get('lastName')
        username = request.POST.get('username')
        correo = request.POST.get('email')
        password = request.POST.get('password')
        confirmar = request.POST.get('password2')

        if password != confirmar:
            messages.error(request, "Las contraseñas no coinciden")
            return redirect('registro')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "El nombre de usuario ya existe")
            return redirect('registro')

        User.objects.create_user(
            first_name=nombre,
            last_name=apellido,
            username=username,
            email=correo,
            password=password
        )

        messages.success(request, "Usuario registrado correctamente")
        return redirect('login')
    return render(request, 'menu/registro.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login_user(request, user)
            return redirect('/') 
        else:
            return render(request, 'menu/login.html', {'error': 'Credenciales incorrectas'})
    return render(request, 'menu/login.html')

@login_required(login_url='login')
def cerrar_sesion(request):
    logout(request)
    return redirect('index')

@login_required(login_url='login')
def terror(request):
    return render(request, 'categorias/terror.html')

@login_required(login_url='login')
def supervivencia(request):
    return render(request, 'categorias/supervivencia.html')

@login_required(login_url='login')
def deportes(request):
    return render(request, 'categorias/deportes.html')

@login_required(login_url='login')
def accion(request):
    return render(request, 'categorias/accion.html')

@login_required(login_url='login')
def mundo_abierto(request):
    return render(request, 'categorias/mundo_abierto.html')

@login_required(login_url='login')
def carreras(request):
    return render(request, 'categorias/carreras.html')

def reinicio_pass(request):
    return render(request, 'menu/reinicio_pass.html')

# Juegos de Terror

@login_required(login_url='login')
def resident_evil_village(request):
    juego = get_object_or_404(Juego, nombre="Resident Evil Village")
    return render(request, 'preview_juegos/preview_rv.html', {'juego': juego})

@login_required(login_url='login')
def outlast(request):
    juego = get_object_or_404(Juego, nombre="Outlast")
    return render(request, 'preview_juegos/preview_ol.html', {'juego': juego})

@login_required(login_url='login')
def resident_evil(request):
    juego = get_object_or_404(Juego, nombre="Resident Evil 6")
    return render(request, 'preview_juegos/preview_rev6.html', {'juego': juego})


# Juegos de Acción

@login_required(login_url='login')
def helldivers(request):
    juego = get_object_or_404(Juego, nombre="Helldivers II")
    return render(request, 'preview_juegos/preview_hd.html', {'juego': juego})

@login_required(login_url='login')
def split_fiction(request):
    juego = get_object_or_404(Juego, nombre="Split Fiction")
    return render(request, 'preview_juegos/preview_sf.html', {'juego': juego})

@login_required(login_url='login')
def elden_ring(request):
    juego = get_object_or_404(Juego, nombre="Elden Ring")
    return render(request, 'preview_juegos/preview_er.html', {'juego': juego})


# Juegos de Mundo Abierto

@login_required(login_url='login')
def ark(request):
    juego = get_object_or_404(Juego, nombre="ARK Ascended")
    return render(request, 'preview_juegos/preview_ark.html', {'juego': juego})

@login_required(login_url='login')
def gta(request):
    juego = get_object_or_404(Juego, nombre="GTA V")
    return render(request, 'preview_juegos/preview_gta.html', {'juego': juego})

@login_required(login_url='login')
def monster_hunter(request):
    juego = get_object_or_404(Juego, nombre="Monster Hunter Wild")
    return render(request, 'preview_juegos/preview_mh.html', {'juego': juego})


# Juegos de Carreras

@login_required(login_url='login')
def ndfs(request):
    juego = get_object_or_404(Juego, nombre="Need for Speed Heat")
    return render(request, 'preview_juegos/preview_ndfs.html', {'juego': juego})

@login_required(login_url='login')
def most_wanted(request):
    juego = get_object_or_404(Juego, nombre="Need for Speed Most Wanted")
    return render(request, 'preview_juegos/preview_nfsmw.html', {'juego': juego})

@login_required(login_url='login')
def f124(request):
    juego = get_object_or_404(Juego, nombre="F1®24")
    return render(request, 'preview_juegos/preview_f21.html', {'juego': juego})


# Juegos de Deportes

@login_required(login_url='login')
def fifa(request):
    juego = get_object_or_404(Juego, nombre="FIFA 2022")
    return render(request, 'preview_juegos/preview_futb.html', {'juego': juego})

@login_required(login_url='login')
def captain_tsubasa(request):
    juego = get_object_or_404(Juego, nombre="Captain Tsubasa")
    return render(request, 'preview_juegos/preview_tsubasa.html', {'juego': juego})

@login_required(login_url='login')
def nba(request):
    juego = get_object_or_404(Juego, nombre="NBA 2K24")
    return render(request, 'preview_juegos/preview_nba.html', {'juego': juego})


# Juegos de Supervivencia

@login_required(login_url='login')
def minecraft(request):
    juego = get_object_or_404(Juego, nombre="Minecraft")
    return render(request, 'preview_juegos/preview_minecraft.html', {'juego': juego})

@login_required(login_url='login')
def rust(request):
    juego = get_object_or_404(Juego, nombre="Rust")
    return render(request, 'preview_juegos/preview_rust.html', {'juego': juego})

@login_required(login_url='login')
def the_forest(request):
    juego = get_object_or_404(Juego, nombre="The Forest")
    return render(request, 'preview_juegos/preview_forest.html', {'juego': juego})

# Carrito de compras
@login_required
def agregar_al_carrito(request, juego_id):
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
    juego = get_object_or_404(Juego, pk=juego_id)

    item, creado = ItemCarrito.objects.get_or_create(
        carrito=carrito,
        juego=juego,
        defaults={'cantidad': 1}
    )
    if not creado:
        item.cantidad += 1
        item.save()

    return redirect(request.META.get('HTTP_REFERER', '/'))