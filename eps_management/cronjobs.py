from django.conf import settings
import requests
import pprint
from user_management.models import Company
from eps_management.models import EpsTotal, EpsLogSource, Notification
from log_source.models import LogSource

table_hexadecimal = [
{'caracter':' ',	'cod_decimal': '&#32;', 'descripcion': 'espacio',           'hexadecimal': '%20'},
{'caracter':'"',	'cod_decimal': '&#34;', 'descripcion': 'obles comillas',    'hexadecimal': '%22'},
{'caracter':'&',	'cod_decimal': '&#38;', 'descripcion': 'mpersand',          'hexadecimal': '%26'},
{'caracter':'(',	'cod_decimal': '&#40;', 'descripcion': 'cerrar paréntesis', 'hexadecimal': '%28'},
{'caracter':')',	'cod_decimal': '&#41;', 'descripcion': 'abrir paréntesis',  'hexadecimal': '%29'},
{'caracter':',',	'cod_decimal': '&#44;', 'descripcion': 'coma',              'hexadecimal': '%2C'},
{'caracter':'/',	'cod_decimal': '&#47;', 'descripcion': 'barra de división', 'hexadecimal': '%2F'},
{'caracter':'=',	'cod_decimal': '&#61;', 'descripcion': 'Igual',             'hexadecimal': '%3D'},
]




def import_new_eps():
    print('llega')
    password = settings.API_GET_PASSWORD
    print('llega')


    for company in Company.objects.all():
        print()

        print('llega')
        query_bice = 'SELECT LOGSOURCENAME(logsourceid) AS "Log Source", SUM(eventcount) AS "Number of Events in Interval", SUM(eventcount) / 60 AS "EPS in Interval" FROM events where domainid=' + str(company.domain_id_qradar) + ' GROUP BY "Log Source" ORDER BY "EPS in Interval" DESC LAST 1 MINUTES'


        headers = {
            'Content-type': 'application/json',
            'accept':'application/json',
            'SEC': password}

        for i in table_hexadecimal:
            query_bice = query_bice.replace(i['caracter'], i['hexadecimal'])
        
        url_query_expression = str(settings.API_URL_BASIC) + 'ariel/searches?query_expression=' + query_bice
        response_url_query_expression = requests.post(url_query_expression, verify=False, headers=headers)
        
        print('Create Search')
        pprint.pprint(response_url_query_expression.json())
        print()
        print()
        print()
        print(str(response_url_query_expression.json()['search_id']))
        print()
        print()
        print()

        url_search = str(settings.API_URL_BASIC) + 'ariel/searches/' + str(response_url_query_expression.json()['search_id']) + '/results'

        url_delete = str(settings.API_URL_BASIC) + 'ariel/searches/' + str(response_url_query_expression.json()['search_id'])

        print('Find Search')
        try:
            import time
            time.sleep(2)
            response_url_search = requests.get(url_search, verify=False, headers=headers)
        except Exception as e:
            response_url_search = requests.get(url_search, verify=False, headers=headers)

        pprint.pprint(response_url_search)

        lista_log = []
        lista_log = []
        suma_eps_intervale = 0
        suma_eps_range = 0
        for events in response_url_search.json()['events']:
            logSource = LogSource.objects.get_or_create(
                name_log_source     = events['Log Source'],
                company             = company
            )[0]

            logSource.save()


            eEpsLogSource = EpsLogSource.objects.create(
                name_log_source     = logSource,
                company             = company,
                count_range         = events['Number of Events in Interval'],
                count_intervale     = events['EPS in Interval'],
            )

            lista_log.append(eEpsLogSource)

            suma_eps_intervale  += int(events['EPS in Interval'])
            suma_eps_range  += int(events['Number of Events in Interval'])




        epsTotal = EpsTotal.objects.create(
            company             = company,
            count_range         = suma_eps_range,
            count_intervale     = suma_eps_intervale,
        )


        for sourceog in lista_log:
            epsTotal.eps_log_source.add(sourceog)
            epsTotal.save()


        notificacion = Notification.objects.filter(
            company = company
        )

        for noti in notificacion:
            epsTotal.notification.add(noti)
            epsTotal.save()


        pprint.pprint(response_url_search.json())

        print('Delete Search')
        response_url_delete = requests.delete(url_delete, verify=False, headers=headers)
        pprint.pprint(response_url_delete.json())




