from django.conf import settings
import requests
import pprint
from user_management.models import Company
from eps_management.models import EpsTotal, EpsLogSource, Notification, EpsERCAllMcafee, EPS_DS_Collection_Rate, EPS_DS_Parsing_Rate
from log_source.models import LogSource
from bs4 import BeautifulSoup


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
    password = settings.API_GET_PASSWORD

    for company in Company.objects.filter(is_search = True):

        query_bice = 'SELECT LOGSOURCENAME(logsourceid) AS "Log Source", SUM(eventcount) AS "Number of Events in Interval", SUM(eventcount) / 180 AS "EPS in Interval" FROM events where domainid=' + str(company.domain_id_qradar) + ' GROUP BY "Log Source" ORDER BY "EPS in Interval" DESC LAST 3 MINUTES'


        headers = {
            'Content-type': 'application/json',
            'accept':'application/json',
            'SEC': password}

        for i in table_hexadecimal:
            query_bice = query_bice.replace(i['caracter'], i['hexadecimal'])
        
        url_query_expression = str(settings.API_URL_BASIC) + 'ariel/searches?query_expression=' + query_bice
        response_url_query_expression = requests.post(url_query_expression, verify=False, headers=headers)
        
        print('Create Search')

        url_search = str(settings.API_URL_BASIC) + 'ariel/searches/' + str(response_url_query_expression.json()['search_id']) + '/results'

        url_delete = str(settings.API_URL_BASIC) + 'ariel/searches/' + str(response_url_query_expression.json()['search_id'])

        print('Find Search')
        try:
            import time
            time.sleep(2)
            response_url_search = requests.get(url_search, verify=False, headers=headers)
        except Exception as e:
            response_url_search = requests.delete(url_delete, verify=False, headers=headers)

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




def import_new_eps_mcafee():
    url_base = "http://172.24.80.68:8000/EPS/"
    html = requests.get(url_base).text
    soup = BeautifulSoup(html, 'lxml')
    jobs = soup.find_all('a')
    import json
    
    for i in jobs:
        if "../" in i.text:
            continue
        
        url_endpoint = url_base + str(i.text)
        data_enpoint = requests.get(url_endpoint).text
        dic_end = json.loads(data_enpoint)

        cliente = str(i.text).split("_")[0]

        company = Company.objects.get(name = cliente)
        
        epsERCAllMcafee = EpsERCAllMcafee.objects.get_or_create(
            company                   =   company,
            erc_collection_rate       =   dic_end['erc_collection_rate'],
            erc_parsing_rate          =   dic_end['erc_parsing_rate'],
            created_date              =   dic_end['time']
        )[0]

        epsERCAllMcafee.save()

        # pprint.pprint(dic_end)

        for j in dic_end['ds_collection_rate'].keys():
            log_source = LogSource.objects.get(
                number_log_source   = j,
                company             = company
            )


            eps_ds_collection_rate = EPS_DS_Collection_Rate.objects.get_or_create(
                company                 =   company,
                ds_collection_rate      =   dic_end['ds_collection_rate'][j],
                created_date            =   dic_end['time'],
                epsercallmcafee         =   epsERCAllMcafee,
                log_source              = log_source
            )[0]

            eps_ds_collection_rate.save()



        for k in dic_end['ds_parsing_rate'].keys():
            log_source = LogSource.objects.get(
                number_log_source   = j,
                company             = company
            )


            eps_ds_parsing_rate = EPS_DS_Parsing_Rate.objects.get_or_create(
                company                 =   company,
                ds_parsing_rate      =   dic_end['ds_collection_rate'][k],
                created_date            =   dic_end['time'],
                epsercallmcafee         =   epsERCAllMcafee,
                log_source              =   log_source
            )[0]

            eps_ds_parsing_rate.save()