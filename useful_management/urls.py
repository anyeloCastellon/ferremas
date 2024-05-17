# useful_management/urls.py
from django.urls import path
from .views import ContactoCreateView
from django.views.generic import TemplateView

urlpatterns = [
    path('contacto/', ContactoCreateView.as_view(), name='contacto_create'),
    path('contacto/success/', TemplateView.as_view(template_name='contacto_success.html'), name='contacto_success'),
]
