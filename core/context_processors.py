from rest_api.models import Carrito

def carrito_count(request):
    if request.user.is_authenticated:
        carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
        count = carrito.items.count()
    else:
        count = 0
    return {'carrito_count': count}
