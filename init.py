from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent
os.environ.setdefault("DJANGO_SETTINGS_MODULE","eps.settings")
import django
from django.conf import settings    
django.setup()


import requests
import pprint
from user_management.models import Company
from log_source.models import LogSource
from user_management.models import Company, TypeCompany, SIEM

import subprocess
import pandas as pd


COMPANY = [
	{'abbreviation': 'LMINA', 'name': 'LMINA', 'type': 'Minería', 'siem': 'McAfee', 'is_search': False},
	{'abbreviation': 'AMSA', 'name': 'AMSA', 'type': 'Minería', 'siem': 'McAfee', 'is_search': False},
	{'abbreviation': 'DTRB', 'name': 'DTRB', 'type': 'Gobierno', 'siem': 'McAfee', 'is_search': False},
	{'abbreviation': 'Salco', 'name': 'Salco', 'type': 'Farmacéutica', 'siem': 'McAfee', 'is_search': False},
	{'abbreviation': 'SCSC', 'name': 'SCSC', 'type': 'Financiera', 'siem': 'McAfee', 'is_search': False},
	{'abbreviation': 'UST', 'name': 'UST', 'type': 'Educación', 'siem': 'McAfee', 'is_search': False},
	{'abbreviation': 'MTS', 'name': 'MTS', 'type': 'Construcción e Ingenieros', 'siem': 'McAfee', 'is_search': False},
	{'abbreviation': 'CMF', 'name': 'CMF', 'type': 'Financiera', 'siem': 'McAfee', 'is_search': False},
	{'abbreviation': 'TRELEC', 'name': 'TRELEC', 'type': 'Energia', 'siem': 'McAfee', 'is_search': False},
	{'abbreviation': 'BCSC', 'name': 'BCSC', 'type': 'Financiera', 'siem': 'McAfee', 'is_search': False},
	{'abbreviation': 'PDI', 'name': 'PDI', 'type': 'Gobierno', 'siem': 'McAfee', 'is_search': False},
	{'abbreviation': 'CDCH', 'name': 'CDCH', 'type': 'Gobierno', 'siem': 'McAfee', 'is_search': False},
	{'abbreviation': 'ENJOY', 'name': 'ENJOY', 'type': 'Casino', 'siem': 'McAfee', 'is_search': False},
	{'abbreviation': 'SNPC', 'name': 'SNPC', 'type': 'Gobierno', 'siem': 'McAfee', 'is_search': False},
	{'abbreviation': 'AMSA', 'name': 'AMSA', 'type': 'Minería', 'siem': 'McAfee', 'is_search': False},
	{'abbreviation': 'CMF', 'name': 'CMF', 'type': 'Gobierno', 'siem': 'McAfee', 'is_search': False},
	{'abbreviation': 'EGT', 'name': 'EGT', 'type': 'Transporte y Logistica', 'siem': 'McAfee', 'is_search': False},
	{'abbreviation': 'JNJ', 'name': 'JNJ', 'type': 'Gobierno', 'siem': 'McAfee', 'is_search': False},
	{'abbreviation': 'MOP', 'name': 'MOP', 'type': 'Gobierno', 'siem': 'McAfee', 'is_search': False},

]

TYPE_COMPANY = [
    'Financiera', 
    'Bancaria', 
    'Gobierno', 
    'Construcción e Ingenieros', 
    'Negocio y Profesional', 
    'Alta tecnología', 
    'Salud', 
    'Retail', 
    'Hostelería', 
    'Transporte y Logistica', 
    'Telecomunicaciones', 
    'Educación', 
    'Energia', 
    'Entretenimiento y medios', 
    'Minería', 
    'Farmacéutica',
    'Casino',
    'Alimenticia'
    ]

SIEM_LIST = ['McAfee', 'Qradar']


def addTypeCompany():
	for i in TYPE_COMPANY:
		type_company = TypeCompany.objects.get_or_create(
			name = i,
		)[0]

		type_company.save()



def addSIEM():
	for i in SIEM_LIST:
		siem = SIEM.objects.get_or_create(
			name = i,
		)[0]

		siem.save()


def addCompany():
	for i in range(len(COMPANY)):
		
		type_company = TypeCompany.objects.get_or_create(
			name			= COMPANY[i]['type'],
		)[0]

		type_company.save()


		siem = SIEM.objects.get_or_create(
			name			= COMPANY[i]['siem'],
		)[0]

		siem.save()


		company = Company.objects.get_or_create(
			name			= COMPANY[i]['name'],
			type_company	= type_company,
			siem 			= siem,
			abbreviation 	= COMPANY[i]['abbreviation'],
			is_search 	= COMPANY[i]['is_search']
		)[0]

		company.save()



if __name__ == '__main__':

	print("Add TypeCompany")
	addTypeCompany()

	print("Add SIEM")
	addSIEM()

	print("Add Company")
	addCompany()
	