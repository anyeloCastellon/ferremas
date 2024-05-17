from rest_framework import serializers
from .models import Categoria, Producto, PrecioProducto

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'name',)

class PrecioProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrecioProducto
        fields = ['fecha', 'valor']

class ProductoSerializer(serializers.ModelSerializer):
    precios = PrecioProductoSerializer(many=True, read_only=True)
    categoria = CategoriaSerializer(source='cat', read_only=True)

    class Meta:
        model = Producto
        fields = ['codigo_producto', 'marca', 'codigo', 'name', 'stock', 'categoria', 'precios', 'imagen']
