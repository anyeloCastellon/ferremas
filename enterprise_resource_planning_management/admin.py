# Register your models here.


from django.contrib import admin
from .models import Categoria, Producto

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'desc')
    search_fields = ('name',)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo_producto', 'marca', 'codigo', 'name', 'cat', 'stock')
    list_editable = ('stock',)
    search_fields = ('name', 'cat__name')
    list_filter = ('cat',)

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
