
from rest_framework import serializers
from datetime import datetime, date, timedelta
from django.utils import timezone
from .models import *
from user_management.serializers import CompanyModelSerializerMinumus, CompanyModelSerializerMaxMinumus
from log_source.serializers import LogSourcePowerBySerializer, LogSourceMinimusPowerBySerializer

class EPSQRadarSerializer(serializers.Serializer):
    eps_serializer = serializers.SerializerMethodField('get_count_desface')

    def get_count_desface(self, obj):
        count = 0
        hora = ""
        this_hour = timezone.now()
        one_hour_later = this_hour - timedelta(hours=4)

        eps = EpsTotal.objects.filter(
            company__name=obj.name,
            created_date__gte=one_hour_later,
            created_date__lte=this_hour,
        ).order_by('-created_date')[:20]

        eps = reversed(eps)

        count_range = []
        count_intervale = []
        created_date = []

        for i in eps:
            count_range.append(i.count_range)
            count_intervale.append(i.count_intervale)
            dia = str(i.created_date).split(' ')[0]
            hora = str(int(str(i.created_date).split(' ')[1].split('.')[0].split(':')[0]) - 3)
            minutos = str(i.created_date).split(' ')[1].split('.')[0].split(':')[1]
            created_date.append(dia + " " + hora + ":" + minutos)

        return {
            "cliente": obj.name,
            "count_range": count_range,
            "count_intervale": count_intervale,
            "created_date": created_date
        }








class EPSAllQRadarSerializer(serializers.Serializer):
    eps_serializer = serializers.SerializerMethodField('get_count_desface')

    def get_count_desface(self, obj):
        count = 0
        hora = ""
        this_hour = timezone.now()
        one_hour_later = this_hour - timedelta(hours=4)

        eps = EpsTotal.objects.filter(
            company__name=obj.name,
            created_date__gte=one_hour_later,
            created_date__lte=this_hour,
        ).order_by('-created_date')[:20]

        eps = reversed(eps)

        count_range = []
        count_intervale = []
        created_date = []

        for i in eps:
            count_range.append(i.count_range)
            count_intervale.append(i.count_intervale)
            dia = str(i.created_date).split(' ')[0]
            hora = str(int(str(i.created_date).split(' ')[1].split('.')[0].split(':')[0]) - 3)
            minutos = str(i.created_date).split(' ')[1].split('.')[0].split(':')[1]
            created_date.append(dia + " " + hora + ":" + minutos)

        return {
            "cliente": obj.name,
            "count_range": count_range,
            "count_intervale": count_intervale,
            "created_date": created_date
        }






class EPS_DS_Collection_RatePowerBySerializer(serializers.ModelSerializer):
    log_source = LogSourceMinimusPowerBySerializer()
    
    class Meta:
        model = EPS_DS_Collection_Rate
        fields = ['ds_collection_rate', 'log_source']




class EPS_DS_Parsing_RatePowerBySerializer(serializers.ModelSerializer):
    log_source = LogSourceMinimusPowerBySerializer()
    
    class Meta:
        model = EPS_DS_Parsing_Rate
        fields = ['ds_parsing_rate', 'log_source']



class EpsERCMinumisMcafeePowerBySerializer(serializers.ModelSerializer):
    company = CompanyModelSerializerMaxMinumus()
    
    class Meta:
        model = EpsERCAllMcafee
        fields = ['id_epsercallmcafee','company', 'erc_collection_rate', 'erc_parsing_rate', 'created_date']





class EpsERCAllMcafeePowerBySerializer(serializers.ModelSerializer):
    company = CompanyModelSerializerMaxMinumus()
    eps_ds_collection_rate_epsercallmcafee = EPS_DS_Collection_RatePowerBySerializer(many=True)
    eps_ds_parsing_rate_epsercallmcafee = EPS_DS_Parsing_RatePowerBySerializer(many=True)
    
    class Meta:
        model = EpsERCAllMcafee
        fields = ['id_epsercallmcafee','company', 'erc_collection_rate', 'erc_parsing_rate', 'created_date', 'eps_ds_collection_rate_epsercallmcafee', 'eps_ds_parsing_rate_epsercallmcafee']



class EPSQRadarPowerBySerializer(serializers.ModelSerializer):
    company = CompanyModelSerializerMinumus()
    
    class Meta:
        model = EpsTotal
        fields = ['id_epstotal','company', 'count_range', 'count_intervale', 'created_date']







class EpsLogSourceQRadarPowerBySerializer(serializers.ModelSerializer):
    company = CompanyModelSerializerMinumus()
    name_log_source = LogSourcePowerBySerializer()
    
    class Meta:
        model = EpsLogSource
        fields = ['id_epslogsource','name_log_source', 'company', 'count_range', 'count_intervale', 'created_date']
