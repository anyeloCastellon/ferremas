import os
import django
import random
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eps.settings')
django.setup()

from enterprise_resource_planning_management.models import Categoria, Producto, PrecioProducto  # Cambia 'tu_app' y 'tu_proyecto' por los nombres reales

def crear_categorias_y_productos():
    # Estructura de datos con categorías y productos
    categorias = {
        'Herramientas': {
            'Herramientas Manuales': ['Martillos', 'Destornilladores', 'Llaves'],
            'Herramientas Eléctricas': ['Taladros', 'Sierras', 'Lijadoras']
        },
        'Materiales de Construcción': {
            'Materiales Básicos': ['Cemento', 'Arena', 'Ladrillos'],
            'Acabados': ['Pinturas', 'Barnices', 'Cerámicos']
        },
        'Equipos de Seguridad': ['Casos', 'Guantes', 'Lentes de Seguridad'],
        'Accesorios Varios': ['Tornillos y Anclajes', 'Fijaciones y Adhesivos', 'Equipos de Medición']
    }

    marcas = ['Bosch', 'Makita', 'Stanley', '3M', 'Samsung']

    for categoria_principal, subcategorias in categorias.items():
        if isinstance(subcategorias, dict):
            for subcategoria, productos in subcategorias.items():
                cat_obj, _ = Categoria.objects.get_or_create(name=subcategoria)
                crear_productos(cat_obj, productos, marcas)
        else:
            cat_obj, _ = Categoria.objects.get_or_create(name=categoria_principal)
            crear_productos(cat_obj, subcategorias, marcas)

def crear_productos(categoria, productos, marcas):
    for producto in productos:
        for _ in range(3):
            codigo_producto = f'{producto[:3].upper()}-{random.randint(100, 999)}'
            prod_obj = Producto.objects.create(
                codigo_producto=codigo_producto,
                marca=random.choice(marcas),
                codigo=f'{producto[:3].upper()}-{random.randint(1000, 9999)}',
                name=producto,
                cat=categoria,
                stock=random.randint(1, 100)
            )
            PrecioProducto.objects.create(
                producto=prod_obj,
                fecha=datetime.now(),
                valor=random.randint(5000, 500000)
            )

if __name__ == '__main__':
    crear_categorias_y_productos()
