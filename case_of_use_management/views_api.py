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

from django.db import connection
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CaseOfUseDataSerializer

class CaseOfUseDataView(APIView):

    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT id_case_of_use, name_case_of_use, is_created, umc.name as name_company, umtc.name as name_typecompany, ihmti.name_type_incident, ihmi.name_incident, ums.name as name_siem, coumtt.name_type_tech, coumtr.name_type_rule
                FROM case_of_use_management_caseuse as cumc
                INNER JOIN case_of_use_management_caseuse_company as cumcuc ON cumcuc.caseuse_id = cumc.id_case_of_use
                INNER JOIN user_management_company as umc ON umc.id_company = cumcuc.company_id
                INNER JOIN user_management_typecompany as umtc ON umtc.id_typecompany = umc.type_company_id
                INNER JOIN case_of_use_management_caseuse_type_incident as coumcuti ON coumcuti.caseuse_id = cumc.id_case_of_use
                INNER JOIN incident_handler_management_typeincident as ihmti ON ihmti.id_type_incident = coumcuti.typeincident_id
                INNER JOIN case_of_use_management_caseuse_incident as coumcui ON coumcui.caseuse_id = cumc.id_case_of_use
                INNER JOIN incident_handler_management_incident as ihmi ON ihmi.id_incident = coumcui.incident_id
                INNER JOIN case_of_use_management_caseuse_siem as coumcus ON coumcus.caseuse_id = cumc.id_case_of_use
                INNER JOIN user_management_siem as ums ON ums.id_siem = coumcus.siem_id
                INNER JOIN case_of_use_management_caseuse_type_tech as coumcutt ON coumcutt.caseuse_id = cumc.id_case_of_use
                INNER JOIN case_of_use_management_typetech as coumtt ON coumtt.id_type_tech = coumcutt.typetech_id
                INNER JOIN case_of_use_management_caseuse_type_rule as coumcutr ON coumcutr.caseuse_id = cumc.id_case_of_use
                INNER JOIN case_of_use_management_typerule as coumtr ON coumtr.id_type_rule = coumcutr.typerule_id
                ORDER BY id_case_of_use
            """)
            columns = [col[0] for col in cursor.description]
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return Response(data)