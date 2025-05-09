from rest_framework import serializers
from .models import Categoria, Juego, Carrito, ItemCarrito

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

class ItemCarritoSerializer(serializers.ModelSerializer):
    juego = serializers.SerializerMethodField(read_only=True)
    juego_id = serializers.PrimaryKeyRelatedField(
        queryset=Juego.objects.all(),
        source='juego',
        write_only=True,
        label='ID de juego'
    )

    class Meta:
        model = ItemCarrito
        fields = [
            'id',
            'juego',
            'juego_id',
            'cantidad',
        ]

    def get_juego(self, obj):
        from .serializers import JuegoSerializer
        return JuegoSerializer(obj.juego).data

class CarritoSerializer(serializers.ModelSerializer):
    items = ItemCarritoSerializer(many=True, read_only=True)
    total = serializers.SerializerMethodField()
    class Meta:
        model = Carrito
        fields = [
            'id',
            'items',
            'total',
            'creado_en',
            'actualizado_en',
        ]
        read_only_fields = ['creado_en', 'actualizado_en']

    def get_total(self, carrito):
        return sum(
            item.cantidad *
            (item.juego.precio_oferta or item.juego.precio_original)
            for item in carrito.items.all()
        )