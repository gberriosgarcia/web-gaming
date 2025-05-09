from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions, status

from django.shortcuts import get_object_or_404

from .services import get_steam_app_details,get_steam_top_sellers
from .models import Categoria, Juego, Carrito, ItemCarrito
from .serializers import CategoriaSerializer, JuegoSerializer, CarritoSerializer, ItemCarritoSerializer

class CategoriaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class JuegoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Juego.objects.all()
    serializer_class = JuegoSerializer

class SteamTopSellersAPIView(APIView):
    def get(self, request):
        top10 = get_steam_top_sellers(limit=10)
        return Response(top10)
    
class SteamAppDetailAPIView(APIView):
    def get(self, request, app_id):
        detalle = get_steam_app_details(app_id)
        if not detalle:
            return Response(
                {"detail": f"No se encontró detalle para app_id {app_id}"},
                status=status.HTTP_404_NOT_FOUND
            )
        return Response(detalle)

class CarritoAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    # Obtener carrito
    def get(self, request):
        carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
        serializer = CarritoSerializer(carrito)
        return Response(serializer.data)

    # Eliminar carrito
    def delete(self, request):
        carrito = get_object_or_404(Carrito, usuario=request.user)
        carrito.items.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ItemCarritoAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    # Guardar elemento crrito
    def post(self, request):
        carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
        serializer = ItemCarritoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        juego = serializer.validated_data['juego']
        cantidad = serializer.validated_data['cantidad']

        item, creado = ItemCarrito.objects.get_or_create(
            carrito=carrito,
            juego=juego,
            defaults={'cantidad': cantidad}
        )
        if not creado:
            item.cantidad = cantidad
            item.save()

        return Response(ItemCarritoSerializer(item).data, status=status.HTTP_201_CREATED)

    # Actualizar elemento carrito
    def patch(self, request, pk):
        carrito = get_object_or_404(Carrito, usuario=request.user)
        item = get_object_or_404(ItemCarrito, pk=pk, carrito=carrito)

        serializer = ItemCarritoSerializer(item, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(ItemCarritoSerializer(item).data)

    # Eliminar elemento carrito
    def delete(self, request, pk):
        carrito = get_object_or_404(Carrito, usuario=request.user)
        item = get_object_or_404(ItemCarrito, pk=pk, carrito=carrito)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)