from django.shortcuts import render
from rest_framework import viewsets
from .models import Categoria, Producto
from .serializers import CategoriaSerializer, ProductoSerializer

from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy



class CategoriaViewSet(viewsets.ModelViewSet):
	queryset = Categoria.objects.all()
	serializer_class = CategoriaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
	queryset = Producto.objects.all()
	serializer_class = ProductoSerializer



class ProductoNoDisponibleBodegaViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Producto.objects.filter(stock=0)  # Productos con stock mayor a cero
	serializer_class = ProductoSerializer









class ProductListView(ListView):
	model = Producto
	template_name = 'product/list.html'

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Listado de Productos'
		context['list_url'] = reverse_lazy('erp:product_list')
		context['entity'] = 'Productos'
		return context