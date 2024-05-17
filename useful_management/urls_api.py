from django.urls import path
from .views import ContactoCreateAPIView

urlpatterns = [
    path('contacto/', ContactoCreateAPIView.as_view(), name='create-contacto'),
]