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


class MyCustomIncidentView(APIView):

    def get(self, request, company_id):
        with connection.cursor() as cursor:
            cursor.execute(f"""
                    SELECT
                        ihmi.name_incident as "Nombre Incidente",
                        ihmi.number_of_use_cases as "# Incidentes cubiertos",
                        COUNT(DISTINCT assigned_cases.id_case_of_use) as "# Incidentes asigandos",
                        (COUNT(DISTINCT assigned_cases.id_case_of_use) * 100.0 / ihmi.number_of_use_cases) as "% Asigando"
                    FROM incident_handler_management_incident as ihmi
                    LEFT JOIN (
                        SELECT coumcui.incident_id, coumcu.id_case_of_use
                        FROM case_of_use_management_caseuse_incident as coumcui
                        INNER JOIN case_of_use_management_caseuse as coumcu ON coumcui.caseuse_id = coumcu.id_case_of_use
                        INNER JOIN case_of_use_management_caseuse_company as coumcuc ON coumcu.id_case_of_use = coumcuc.caseuse_id
                        WHERE coumcuc.company_id = {company_id}
                    ) as assigned_cases ON ihmi.id_incident = assigned_cases.incident_id
                    WHERE ihmi.number_of_use_cases IS NOT NULL
                    GROUP BY ihmi.name_incident, ihmi.number_of_use_cases
                    ORDER BY "% Asigando" DESC;
            """)
            columns = [col[0] for col in cursor.description]
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return Response(data)

