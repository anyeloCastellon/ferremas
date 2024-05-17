from django.urls import path

app_name = 'erp'

from .views import *




urlpatterns = [
    # product
    path('product/list/', ProductListView.as_view(), name='product_list'),
]
