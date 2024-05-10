from django.db import models

# Create your models here.
#Herencia desde un Modelo Base
from base.models import BaseModel

class Categoria(BaseModel):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    desc = models.CharField(max_length=500, null=True, blank=True, verbose_name='Descripción')

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']


class Producto(models.Model):
    codigo_producto = models.CharField(max_length=20, verbose_name='Código del producto', unique=True)
    marca = models.CharField(max_length=50, verbose_name='Marca')
    codigo = models.CharField(max_length=20, verbose_name='Código', unique=True)
    name = models.CharField(max_length=150, verbose_name='Nombre')
    cat = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoría')
    stock = models.IntegerField(default=0, verbose_name='Stock')

    def __str__(self):
        return f'{self.marca} - {self.name}'

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']


class PrecioProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='precios')
    fecha = models.DateTimeField(verbose_name='Fecha')
    valor = models.IntegerField(default=0, verbose_name='Valor')

    class Meta:
        verbose_name = 'Precio del Producto'
        verbose_name_plural = 'Precios de los Productos'
        ordering = ['-fecha']