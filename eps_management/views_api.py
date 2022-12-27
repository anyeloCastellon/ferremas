from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import action

from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from .models import EpsTotal
from .serializers import EPSQRadarSerializer
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

        set_list = list()

        this_hour = timezone.now()
        one_hour_later = this_hour - timedelta(hours=4)

        companies = Company.objects.all()

        initial_date = EpsTotal.objects.filter(
            created_date__gte=one_hour_later,
            created_date__lte=this_hour
            )

        sera = EPSQRadarSerializer(companies, many=True)

        return Response(sera.data)