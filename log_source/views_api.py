from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import action

from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from .models import LogSource
from .serializers import LogSourcePowerBySerializer
from django.utils import timezone
from datetime import datetime, date, timedelta
from user_management.models import Company



class LogSourcePowerByViewSet(viewsets.ModelViewSet):
    queryset = LogSource.objects.all()
    serializer_class = LogSourcePowerBySerializer