
from rest_framework import serializers
from datetime import datetime, date, timedelta
from django.utils import timezone
from .models import *

from rest_framework import serializers

class CaseOfUseDataSerializer(serializers.Serializer):
    id_case_of_use = serializers.IntegerField()
    name_case_of_use = serializers.CharField(max_length=2255)
    is_created = serializers.BooleanField()
    umc_name = serializers.CharField(max_length=255)
    umtc_name = serializers.CharField(max_length=255)
    ihmti_name_type_incident = serializers.CharField(max_length=255)
    ihmi_name_incident = serializers.CharField(max_length=255)
    ums_name = serializers.CharField(max_length=255)
    coumtt_name_type_tech = serializers.CharField(max_length=255)
    coumtr_name_type_rule = serializers.CharField(max_length=255)




