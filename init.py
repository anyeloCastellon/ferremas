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
from incident_handler_management.models import TypeIncident, Incident
from case_of_use_management.models import TypeRule, TypeTech, SignatureCiber, CaseUse

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
	{'abbreviation': 'MTG', 'name': 'MTG', 'type': 'Energía', 'siem': 'Qradar', 'is_search': False},
	{'abbreviation': 'Excon', 'name': 'Excon', 'type': 'Constructura', 'siem': 'Qradar', 'is_search': False},
	{'abbreviation': 'CCI', 'name': 'CCI', 'type': 'CiberInteligencia', 'siem': 'Qradar', 'is_search': False},
	{'abbreviation': 'Bice', 'name': 'Bice', 'type': 'Financiera', 'siem': 'Qradar', 'is_search': False},
	{'abbreviation': 'Autorrentas', 'name': 'Autorrentas', 'type': 'Arriendo', 'siem': 'Qradar', 'is_search': False},
	{'abbreviation': 'Nido', 'name': 'Nido', 'type': 'Estudiantil colegio', 'siem': 'Qradar', 'is_search': False},

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
    'Alimenticia',
	'Aseguradora',
	'CiberInteligencia',
	'Arriendo',
	'Estudiantil colegio',
	'Constructura',
	'Energía',


    ]

SIEM_LIST = ['McAfee', 'Qradar']



TYPE_INCIDENT = [
	"Abusive Content",
	"Malicious Code",
	"Information Gathering",
	"Intrusion Attempts",
	"Intrusions",
	"Availability",
	"Information Content Security",
	"Fraud",
	"Vulnerable",
	"Other"
]


INCIDENT = [
	{"name_type_incident": "Abusive Content", "incident": "Spam"},
	{"name_type_incident": "Abusive Content", "incident": "Harmful Speech"},
	{"name_type_incident": "Abusive Content", "incident": "Child/Sexual/Violence/"},
	{"name_type_incident": "Malicious Code", "incident": "Virus"},
	{"name_type_incident": "Malicious Code", "incident": "Worm"},
	{"name_type_incident": "Malicious Code", "incident": "Trojan"},
	{"name_type_incident": "Malicious Code", "incident": "Spyware"},
	{"name_type_incident": "Malicious Code", "incident": "Dialer"},
	{"name_type_incident": "Malicious Code", "incident": "Rootkit"},
	{"name_type_incident": "Malicious Code", "incident": "Malware"},
	{"name_type_incident": "Malicious Code", "incident": "Botnet drone"},
	{"name_type_incident": "Malicious Code", "incident": "Ransomware"},
	{"name_type_incident": "Malicious Code", "incident": "Malware configuration"},
	{"name_type_incident": "Malicious Code", "incident": "C&C"},
	{"name_type_incident": "Information Gathering", "incident": "Scanning"},
	{"name_type_incident": "Information Gathering", "incident": "Sniffing"},
	{"name_type_incident": "Information Gathering", "incident": "Social Engineering"},
	{"name_type_incident": "Intrusion Attempts", "incident": "Exploiting of known Vulnerabilities"},
	{"name_type_incident": "Intrusion Attempts", "incident": "Login attempts"},
	{"name_type_incident": "Intrusion Attempts", "incident": "New attack signature"},
	{"name_type_incident": "Intrusions", "incident": "Privileged Account Compromise"},
	{"name_type_incident": "Intrusions", "incident": "Unprivileged Account Compromise"},
	{"name_type_incident": "Intrusions", "incident": "Application Compromise"},
	{"name_type_incident": "Intrusions", "incident": "Bot"},
	{"name_type_incident": "Intrusions", "incident": "Defacement"},
	{"name_type_incident": "Intrusions", "incident": "Compromised"},
	{"name_type_incident": "Intrusions", "incident": "Backdoor"},
	{"name_type_incident": "Availability", "incident": "DoS"},
	{"name_type_incident": "Availability", "incident": "DDoS"},
	{"name_type_incident": "Availability", "incident": "Sabotage"},
	{"name_type_incident": "Availability", "incident": "Outage (no malice)"},
	{"name_type_incident": "Information Content Security", "incident": "Unauthorised access to information"},
	{"name_type_incident": "Information Content Security", "incident": "Unauthorised modification of information"},
	{"name_type_incident": "Information Content Security", "incident": "Dropzone"},
	{"name_type_incident": "Fraud", "incident": "Unauthorized use of resources"},
	{"name_type_incident": "Fraud", "incident": "Copyright"},
	{"name_type_incident": "Fraud", "incident": "Masquerade"},
	{"name_type_incident": "Fraud", "incident": "Phishing"},
	{"name_type_incident": "Vulnerable", "incident": "Open for abuse"},
	{"name_type_incident": "Other", "incident": "blacklist"},
	{"name_type_incident": "Other", "incident": "unknown"},

]


TYPE_RULE = [
	"Firma AntiSpam",
	"Indicadores de Compromiso",
	"Firma EDR",
	"Escan Horizontal Perimetral",
	"Escan Horizontal Portales Web",
	"Escan Vertical Perimetral",
	"Escan Vertical Portales Web",
	"Firma Interna",
	"Comportamiento",
	"Navegación riesgosa",
	"Comunicación IoC",
	"UBA",
	"Firma Perimetro",
	"Ruta de explotación Perimetral",
	"Ruta de explotación Portales Web",
	"Firma Portales Web",
	"Comportamiento IoA",
	"Trafico Portales Web",
	"Comportamiento Perimetral",
	"Firma WAF",
	"Firma Perimetral",
	"Firma APPControl",
]



SIGNATURECIBER = [
	"Account Discovery: Domain Account",
	"Active Scanning",
	"Vulnerability Scanning",
	"LLMNR/NBT-NS Poisoning and SMB Relay",
	"ARP Cache Poisoning",
	"DHCP Spoofing",
	"Application Layer Protocol",
	"Web Protocols",
	"File Transfer Protocols",
	"Mail Protocols",
	"DNS",
	"Automated Exfiltration",
	"Compromise Accounts",
	"Data Obfuscation",
	"Defacement",
	"Domain Trust Discovery",
	"Dynamic Resolution",
	"DNS Calculation",
	"Exfiltration Over Alternative Protocol",
	"Exfiltration Over C2 Channel",
	"Exfiltration Over Other Network Medium",
	"Exfiltration Over Web Service",
	"Exploit Public-Facing Application",
	"Exploitation of Remote ServicesD",
	"External Remote Services",
	"Forced Authentication",
	"Group Policy Discovery",
	"Ingress Tool Transfer",
	"Lateral Tool Transfer",
	"Non-Application Layer Protocol",
	"Non-Standard Port",
	"Phishing",
	"Phishing for Information",
	"Protocol Tunneling",
	"Proxy",
	"Remote Access Software",
	"Remote Service Session Hijacking",
	"Server Software Component",
	"Web Shell",
	"User ExecutionUser Execution",
	"Brute Force",
	"Password Guessing",
	"Password Cracking",
	"Password Spraying",
	"Credential Stuffing",
	"Exploitation for Credential Access",
	"Forge Web Credentials: SAML Tokens",
	"Indicator Removal",
	"Modify Authentication Process",
	"Multi-Factor Authentication Request Generation",
	"Unsecured Credentials",
	"Use Alternate Authentication Material",
	"Pass the Hash",
	"Pass the Ticket",
	"Valid Accounts",
	"Default Accounts",
	"Domain Accounts",
	"Local Accounts",
	"Cloud Accounts",
	"Create Account",
	"Local Account",
	"Domain Account",
	"Cloud Account",
	"Hide Artifacts",
	"Hidden Users",
	"Account Manipulation",
	"Additional Cloud Credentials",
	"Additional Email Delegate Permissions",
	"Modify Authentication Process",
	"Steal or Forge Kerberos Tickets",
	"Golden Ticket",
	"Kerberoasting",
	"AS-REP Roasting",
	"OS Credential Dumping",
	"DCSync",
	"Account Manipulation: Device Registration",
	"Domain Policy Modification",
	"Group Policy Modification",
	"File and Directory Permissions Modification",
	"Modify Authentication Process",
	"Multi-Factor Authentication",
	"Web Cookies",
	"Application Access Token",
	"Web Session Cookie",
	"Acquire Infrastructure",
	"Compromise Accounts",
	"Compromise Infrastructure",
	"Drive-by Compromise",
	"Hardware Additions",
	"Replication Through Removable Media",
	"Cloud Administration Command",
	"Command and Scripting Interpreter",
	"PowerShell",
	"AppleScript",
	"Windows Command Shell",
	"Unix Shell",
	"Visual Basic",
	"Python",
	"JavaScript",
	"Exploitation for Client Execution",
	"Scheduled Task/Job",
	"Create or Modify System Process",
	"Internal Spearphishing",
	"Remote Desktop Protocol",
	"SMB/Windows Admin Shares",
	"Distributed Component Object Model",
	"SSH",
	"VNC",
	"Windows Remote Management",
	"Data Transfer Size Limits",
	"Exfiltration to Code Repository"
]




TYPE_TECH = [
	'AntiSpam',
	'EDR',
	'IPS',
	'Firewall Trafico',
	'WAF',
	'Logs Server',
	'URLFiltering',
	'Active Directory',
	'VPN',
	'Proxy',
	'O365',
	'APPControl',
	'Analisis de Red',
	'MSWin',
	'Linux',
	'Cloud Service',
	"Network Traffic",
	'Operational Databases',
	'Web Credential',
	'Command'
]



SIGNATURECIBER

def addSIGNATURECIBER():
	for i in SIGNATURECIBER:
		
		signatureCiber = SignatureCiber.objects.get_or_create(
			name_signature_ciber = i
		)[0]

		signatureCiber.save()


def addTYPE_TECH():
	for i in TYPE_TECH:
		
		typeTech = TypeTech.objects.get_or_create(
			name_type_tech = i
		)[0]

		typeTech.save()



def addTYPE_RULE():
	for i in TYPE_RULE:
		
		typeRule = TypeRule.objects.get_or_create(
			name_type_rule = i
		)[0]

		typeRule.save()


def addIncident():
	for i in range(len(INCIDENT)):
		
		type_incident = TypeIncident.objects.get_or_create(
			name_type_incident			= INCIDENT[i]['name_type_incident'],
		)[0]

		type_incident.save()


		incident = Incident.objects.get_or_create(
			name_incident			= INCIDENT[i]['incident'],
			type_incident			= type_incident
		)[0]

		incident.save()



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
	
	print("Add Incident")
	addIncident()

	print("Add Type Rule")
	addTYPE_RULE()

	print("Add Type Tech")
	addTYPE_TECH()

	print("Add Type Signature")
	addSIGNATURECIBER()