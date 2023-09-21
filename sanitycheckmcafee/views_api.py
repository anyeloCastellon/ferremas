from rest_framework import generics
from .models import RegistroHistorico
from .serializers import RegistroHistoricoSerializer

from datetime import datetime, timedelta

class RegistroHistoricoListView(generics.ListAPIView):
    serializer_class = RegistroHistoricoSerializer

    def get_queryset(self):
        # Fecha límite (hace 30 días)
        fecha_limite = datetime.now() - timedelta(days=5)

        # Filtra los registros basados en el criterio proporcionado
        return RegistroHistorico.objects.filter(
            name_log_source__seguir_escalando=True, 
            estado=False, 
            timestamp__gte=fecha_limite
        )