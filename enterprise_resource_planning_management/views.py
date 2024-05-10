from django.shortcuts import render
from rest_framework import viewsets
from .models import Categoria, Producto
from .serializers import CategoriaSerializer, ProductoSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer



class ProductoDisponibleBodegaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Producto.objects.filter(stock=0)  # Productos con stock mayor a cero
    serializer_class = ProductoSerializer