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

class CaseOfUseDataDynamicCompanyView(APIView):

    def get(self, request, company_id):
        with connection.cursor() as cursor:
            cursor.execute(f"""
                SELECT coumcu.id_case_of_use as "ID Caso de Uso", 
                       coumcu.name_case_of_use as "Nombre Caso de Uso"
                FROM case_of_use_management_caseuse as coumcu
                LEFT JOIN (
                    SELECT caseuse_id
                    FROM case_of_use_management_caseuse_company
                    WHERE company_id = {company_id}
                ) AS assigned_cases ON coumcu.id_case_of_use = assigned_cases.caseuse_id
                WHERE assigned_cases.caseuse_id IS NULL;
            """)
            columns = [col[0] for col in cursor.description]
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return Response(data)


class CaseOfUseTechnologyCoverageView(APIView):

    def get(self, request, company_id):
        with connection.cursor() as cursor:
            cursor.execute(f"""
                SELECT 
                    coumtt.id_type_tech as "ID Tipo de Tecnologia", 
                    coumtt.name_type_tech as "Nombre Tipo de Tecnologia"
                FROM case_of_use_management_typetech as coumtt
                INNER JOIN case_of_use_management_caseuse_type_tech as coumcutt ON coumcutt.typetech_id = coumtt.id_type_tech
                INNER JOIN case_of_use_management_caseuse as cumc ON cumc.id_case_of_use = coumcutt.caseuse_id
                INNER JOIN case_of_use_management_caseuse_company as coumcuc ON cumc.id_case_of_use = coumcuc.caseuse_id
                INNER JOIN user_management_company as umc ON umc.id_company = coumcuc.company_id
                WHERE umc.id_company = {company_id}
                GROUP BY coumtt.id_type_tech
                ORDER BY coumtt.id_type_tech
            """)
            columns = [col[0] for col in cursor.description]
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return Response(data)



class CaseOfUseMissingTechnologyView(APIView):

    def get(self, request, company_id):
        with connection.cursor() as cursor:
            cursor.execute(f"""
                SELECT 
                    coumtt.id_type_tech as "ID Tipo de Tecnologia", 
                    coumtt.name_type_tech as "Nombre Tipo de Tecnologia"
                FROM case_of_use_management_typetech as coumtt
                WHERE coumtt.id_type_tech NOT IN (
                    SELECT DISTINCT coumcutt.typetech_id
                    FROM case_of_use_management_caseuse_type_tech as coumcutt
                    INNER JOIN case_of_use_management_caseuse as coumcu ON coumcutt.caseuse_id = coumcu.id_case_of_use
                    INNER JOIN case_of_use_management_caseuse_company as coucuc ON coumcu.id_case_of_use = coucuc.caseuse_id
                    WHERE coucuc.company_id = {company_id}
                    );
            """)
            columns = [col[0] for col in cursor.description]
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return Response(data)



class CaseOfUseRuleTypeCoverageView(APIView):

    def get(self, request, company_id):
        with connection.cursor() as cursor:
            cursor.execute(f"""
                SELECT 
                    coumtr.id_type_rule as "ID Tipo de Regla", 
                    coumtr.name_type_rule as "Nombre Tipo de Regla"
                FROM case_of_use_management_typerule as coumtr
                INNER JOIN case_of_use_management_caseuse_type_rule as coumcutr ON coumcutr.typerule_id = coumtr.id_type_rule 
                INNER JOIN case_of_use_management_caseuse as cumc ON cumc.id_case_of_use = coumcutr.caseuse_id
                INNER JOIN case_of_use_management_caseuse_company as coumcuc ON cumc.id_case_of_use = coumcuc.caseuse_id
                INNER JOIN user_management_company as umc ON umc.id_company = coumcuc.company_id
                WHERE umc.id_company = {company_id}
                GROUP BY coumtr.id_type_rule
                ORDER BY coumtr.id_type_rule
            """)
            columns = [col[0] for col in cursor.description]
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return Response(data)



class CaseOfUseMissingRuleTypeView(APIView):

    def get(self, request, company_id):
        with connection.cursor() as cursor:
            cursor.execute(f"""
                    SELECT 
                        coumtr.id_type_rule as "ID Tipo de Regla", 
                        coumtr.name_type_rule as "Nombre Tipo de Regla"
                    FROM case_of_use_management_typerule as coumtr
                    LEFT JOIN (
                        SELECT DISTINCT coumcutr.typerule_id
                        FROM case_of_use_management_caseuse_type_rule as coumcutr
                        INNER JOIN case_of_use_management_caseuse as cumc ON coumcutr.caseuse_id = cumc.id_case_of_use
                        INNER JOIN case_of_use_management_caseuse_company as coumcuc ON cumc.id_case_of_use = coumcuc.caseuse_id
                        WHERE coumcuc.company_id = {company_id}
                    ) AS assigned_rules ON coumtr.id_type_rule = assigned_rules.typerule_id
                    WHERE assigned_rules.typerule_id IS NULL;
            """)
            columns = [col[0] for col in cursor.description]
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return Response(data)



class CaseOfUseIncidentCoverageView(APIView):

    def get(self, request, company_id):
        with connection.cursor() as cursor:
            cursor.execute(f"""
                SELECT 
                    ihmi.id_incident as "ID Incidente", 
                    ihmi.name_incident as "Nombre Incidente"
                FROM incident_handler_management_incident as ihmi
                LEFT JOIN (
                    SELECT DISTINCT cucci.incident_id
                    FROM case_of_use_management_caseuse_incident as cucci
                    INNER JOIN case_of_use_management_caseuse as cu ON cucci.caseuse_id = cu.id_case_of_use
                    INNER JOIN case_of_use_management_caseuse_company as cucc ON cu.id_case_of_use = cucc.caseuse_id
                    WHERE cucc.company_id = {company_id}
                ) AS assigned_incidents ON ihmi.id_incident = assigned_incidents.incident_id
                WHERE assigned_incidents.incident_id IS NULL;
            """)
            columns = [col[0] for col in cursor.description]
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return Response(data)




class CaseOfUseMissingIncidentView(APIView):

    def get(self, request, company_id):
        with connection.cursor() as cursor:
            cursor.execute(f"""
                    SELECT 
                        ihmi.id_incident as "ID Incidente", 
                        ihmi.name_incident as "Nombre Incidente"
                    FROM incident_handler_management_incident as ihmi
                    INNER JOIN (
                        SELECT DISTINCT cucci.incident_id
                        FROM case_of_use_management_caseuse_incident as cucci
                        INNER JOIN case_of_use_management_caseuse as cu ON cucci.caseuse_id = cu.id_case_of_use
                        INNER JOIN case_of_use_management_caseuse_company as cucc ON cu.id_case_of_use = cucc.caseuse_id
                        WHERE cucc.company_id = {company_id}
                    ) AS assigned_incidents ON ihmi.id_incident = assigned_incidents.incident_id;
            """)
            columns = [col[0] for col in cursor.description]
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return Response(data)





class CaseOfUseIncidentTypeCoverageView(APIView):

    def get(self, request, company_id):
        with connection.cursor() as cursor:
            cursor.execute(f"""
                SELECT 
                    ihmti.id_type_incident as "ID Tipo de Incidente", 
                    ihmti.name_type_incident as "Nombre Tipo de Incidente"
                FROM incident_handler_management_typeincident as ihmti
                LEFT JOIN (
                    SELECT DISTINCT cucti.typeincident_id
                    FROM case_of_use_management_caseuse_type_incident as cucti
                    INNER JOIN case_of_use_management_caseuse as cu ON cucti.caseuse_id = cu.id_case_of_use
                    INNER JOIN case_of_use_management_caseuse_company as cucc ON cu.id_case_of_use = cucc.caseuse_id
                    WHERE cucc.company_id = {company_id}
                ) AS assigned_incidents ON ihmti.id_type_incident = assigned_incidents.typeincident_id
                WHERE assigned_incidents.typeincident_id IS NULL;
            """)
            columns = [col[0] for col in cursor.description]
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return Response(data)


class CaseOfUseMissingIncidentTypeView(APIView):

    def get(self, request, company_id):
        with connection.cursor() as cursor:
            cursor.execute(f"""
                    SELECT 
                        ihmti.id_type_incident as "ID Tipo de Incidente", 
                        ihmti.name_type_incident as "Nombre Tipo de Incidente"
                    FROM incident_handler_management_typeincident as ihmti
                    INNER JOIN (
                        SELECT DISTINCT cucti.typeincident_id
                        FROM case_of_use_management_caseuse_type_incident as cucti
                        INNER JOIN case_of_use_management_caseuse as cu ON cucti.caseuse_id = cu.id_case_of_use
                        INNER JOIN case_of_use_management_caseuse_company as cucc ON cu.id_case_of_use = cucc.caseuse_id
                        WHERE cucc.company_id = {company_id}
                    ) AS assigned_incidents ON ihmti.id_type_incident = assigned_incidents.typeincident_id;
            """)
            columns = [col[0] for col in cursor.description]
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return Response(data)

