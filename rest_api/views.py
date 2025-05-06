from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import get_steam_app_details,get_steam_top_sellers
from .models import Categoria, Juego
from .serializers import CategoriaSerializer, JuegoSerializer

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