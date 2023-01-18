from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import action

from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from .models import *
from .serializers import *
from django.utils import timezone
from datetime import datetime, date, timedelta
from user_management.models import Company




class EPSViewSet(viewsets.ModelViewSet):
    queryset = EpsTotal.objects.all()
    serializer_class = EPSQRadarSerializer

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            self.queryset.filter(company_id=kwargs['pk']), many=True)
        return Response(serializer.data)



    @action(methods=['get'], detail=False)
    def get_dashboard_initial(self, request, format=None):

        companies = Company.objects.all()

        sera = EPSQRadarSerializer(companies, many=True)
        return Response(sera.data)


    @action(methods=['get'], detail=False)
    def get_dashboard_eps_all(self, request, format=None):

        companies = Company.objects.all()

        sera = EPSQRadarSerializer(companies, many=True)
        return Response(sera.data)


class EPSPowerByViewSet(viewsets.ModelViewSet):
    queryset = EpsTotal.objects.all()
    serializer_class = EPSQRadarPowerBySerializer



class EpsLogSourcePowerByViewSet(viewsets.ModelViewSet):
    queryset = EpsLogSource.objects.all()
    serializer_class = EpsLogSourceQRadarPowerBySerializer



class EpsERCAllMcafeePowerByViewSet(viewsets.ModelViewSet):
    queryset = EpsERCAllMcafee.objects.all()
    serializer_class = EpsERCAllMcafeePowerBySerializer



    @action(methods=['get'], detail=False)
    def get_data_eps_all(self, request, format=None):

        companies = Company.objects.filter(siem__name = 'Mcafee')

        for compamy in companies:
            epsercallmcafee = EpsERCAllMcafee.objects.filter(company__name = compamy.name)
            sera = EpsERCAllWithFormatMcafeePowerBySerializer(epsercallmcafee, many=True)
            
        return Response(sera.data)



class EpsERCMinimusMcafeePowerByViewSet(viewsets.ModelViewSet):
    queryset = EpsERCAllMcafee.objects.all()
    serializer_class = EpsERCMinumisMcafeePowerBySerializer