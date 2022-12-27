from ast import arg
from unicodedata import name
from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_204_NO_CONTENT

# Create your views here.
import  pandas      as pd
from functools import reduce
from pathlib import Path
import re

from geo_management.models import Country, Geolocation, PathURL, TypeListIP 


BASE_DIR = Path(__file__).resolve().parent.parent

LOCALE_IP = pd.read_csv(
						str(BASE_DIR) + "/locale_ip.csv",
						delimiter   = ",",
						header      = None,
						usecols     = [0, 1, 2],
						names       = ['min', 'max', 'country']
						)
LOCALE_GEO = pd.read_csv(
					str(BASE_DIR) + "/locale_geo_and_countries.csv",
					delimiter   = ",",
					header      = None,
					usecols     = [1, 2, 3, 4, 5],
					names       = ['country_id', 'country', 'latitude', 'longitude', 'name_country']
					)



class GeneralModelView(viewsets.ModelViewSet):
    serializer_class = None

    def get_queryset(self):
        model = self.get_serializer().Meta.model
        return model.objects.filter(enabled = True)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if(instance.enabled):
            instance.enabled = False
        else:
            instance.enabled = True
        instance.save()
        return Response(status=HTTP_204_NO_CONTENT)


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset().filter(enabled=True))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        import pprint

        self.add_base_model(request)
        return Response(serializer.data)

    
    def add_base_model(self, request):
        print(request.META)
        print()
        print(request.META.get('HTTP_X_FORWARDED_FOR'))
        ip = str(request.META.get('HTTP_X_FORWARDED_FOR')).split(",")[0]
        print(ip)
        if ip:
            geo = Geolocation.objects.filter(ip_v4 = ip)
            print(geo)
            if(len(geo)==0):
                pais = self.obtener_pais(ip)
                if(pais != None):
                    country = Country.objects.filter(
                        country_name            = pais[3]
                    )

                    typeListIP = TypeListIP.objects.get(name="Visit")

                    if(len(country)>0):
                        geo = Geolocation.objects.create(
                            latitude                = pais[0],
                            longitude               = pais[1],
                            country                 = country[0],
                            typeListIP              = typeListIP,
                            ip_v4                   = ip,
                        )

            try:
                path = PathURL.objects.create(
                    geolocation         = geo[0],
                    user                = request.user,
                    path_back           = request.META.get('PATH_INFO'),
                    path_front          = request.META.get('HTTP_REFERER'),
                    http_referer        = request.META.get('HTTP_SEC_CH_UA_PLATFORM'),
                    http_sec_ch_ua      = request.META.get('HTTP_SEC_CH_UA'),
                    http_user_agent     = request.META.get('HTTP_USER_AGENT'),
                )
            
            except Exception as e:
                print(e)



    regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
			25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
			25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
			25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''
	  

    def check_ip(self, Ip):  
    
        if(re.search(self.regex, Ip)):  
            return True
        else:  
            return False


    def check_ip(self, s):
        try:
            a = s.split('.')
            if len(a) != 4:
                return False
            for x in a:
                if not x.isdigit():
                    return False
                i = int(x)
                if i < 0 or i > 255:
                    return False
            return True
        except Exception as e:
            return False


    def ip_from_string(self, s):
        try:
            return reduce(lambda a,b: a<<8 | b, map(int, s.split(".")))
        except Exception as e:
            print(e)
            return

    def ip_to_string(self, ip):
        return ".".join(map(lambda n: str(ip>>n & 0xFF), [24,16,8,0]))


    def get_country_by_ip_range(self, ip_32_bit_integer):
        data_frame = LOCALE_IP
        search = data_frame.loc[ 
                            (data_frame['min'] <= ip_32_bit_integer) & (data_frame['max'] >= ip_32_bit_integer), 
                            ['min', 'max', 'country'] 
                        ]

        return search['country'].values[0]


    def get_geo_by_country_id(self, country_id):
        data_frame = LOCALE_GEO

        search = data_frame.loc[ 
                            data_frame['country_id'] == country_id, 
                            ['latitude', 'longitude', 'country', 'name_country', 'country_id'] 
                        ]

        return [ float(search.values[0][0]), float(search.values[0][1]) , search.values[0][2], search.values[0][3], search.values[0][4]] 


    def get_geo_and_country_by_ip(self, ip):
        try:
            processed_ip = self.ip_from_string(ip)
            country = self.get_country_by_ip_range(processed_ip)
            if country == '-':
                return None
            else: 
                return self.get_geo_by_country_id(country)
        except Exception as e:
            print(e)
            return

    def obtener_pais(self, ip):
        tmp_result = self.get_geo_and_country_by_ip(ip)
        return tmp_result
