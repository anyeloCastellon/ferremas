from rest_framework import serializers
from .models import RegistroHistorico

from user_management.serializers import CompanyModelSerializerMinumus
from log_source.serializers import LogSourceMinimusPowerBySerializer


class RegistroHistoricoSerializer(serializers.ModelSerializer):
    company = CompanyModelSerializerMinumus()
    name_log_source = LogSourceMinimusPowerBySerializer()

    class Meta:
        model = RegistroHistorico
        fields = ['timestamp','escalado_a', 'comentario', 'company', 'created_date', 'name_log_source']
