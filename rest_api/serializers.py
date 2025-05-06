from rest_framework import serializers
from .models import Categoria, Juego

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre']

class JuegoSerializer(serializers.ModelSerializer):

    categoria_id = serializers.PrimaryKeyRelatedField(
        source='categoria',             
        queryset=Categoria.objects.all(),
        label='Categoría'
    )

    class Meta:
        model = Juego
        fields = [
            'id',
            'categoria_id',
            'nombre',
            'precio_original',
            'precio_oferta',
            'descripcion',
            'ruta_imagen',
        ]
