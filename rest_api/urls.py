from django.urls import path
from .views import CategoriaListCreateAPIView, JuegoListCreateAPIView, SteamAppDetailAPIView, SteamTopSellersAPIView

urlpatterns = [
    path('categorias/', CategoriaListCreateAPIView.as_view(), name='categoria-list-create'),
    path('juegos/',    JuegoListCreateAPIView.as_view(),     name='juego-list-create'),
    path('steam-top-sellers/', SteamTopSellersAPIView.as_view(), name='steam-top-sellers'),
    path('steam-apps/<int:app_id>/', SteamAppDetailAPIView.as_view(), name='steam-app-detail'),
]
