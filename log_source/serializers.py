
from rest_framework import serializers
from datetime import datetime, date, timedelta
from django.utils import timezone
from .models import LogSource
from user_management.serializers import CompanyModelSerializerMinumus




class LogSourcePowerBySerializer(serializers.ModelSerializer):
    company = CompanyModelSerializerMinumus()
    
    class Meta:
        model = LogSource
        fields = ['id_datasource','name_log_source', 'company']
