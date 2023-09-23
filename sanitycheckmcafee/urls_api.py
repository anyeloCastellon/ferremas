from django.urls import path
from .views_api import RegistroHistoricoListView, ejecutar_cronjob

urlpatterns = [
    path('registro-historico/', RegistroHistoricoListView.as_view(), name='registro-historico-list'),
    path('ejecutar-cronjob/', ejecutar_cronjob),
]
