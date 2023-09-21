from django.urls import path
from .views_api import RegistroHistoricoListView

urlpatterns = [
    path('registro-historico/', RegistroHistoricoListView.as_view(), name='registro-historico-list'),
]
