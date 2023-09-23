from pathlib import Path
import os
from django.conf import settings

import requests
import pprint
from user_management.models import Company
from log_source.models import LogSource
from .models import RegistroHistorico
import subprocess
import pandas as pd
import pytz
from datetime import datetime, timedelta

def import_new_sanity_trellix():
    # Definir el comando y los argumentos en una lista
    command = ["esmcheckds2", "-a", "--disabled", "-f", "csv"]

    # Ejecutar el comando y redirigir la salida a un archivo
    with open("./sanity.csv", "w") as f:
        subprocess.run(command, stdout=f)

    df = pd.read_csv('./sanity.csv')

    # Define la zona horaria para Santiago de Chile
    santiago_tz = pytz.timezone('Chile/Continental')

    # Obtener la hora actual en Santiago de Chile
    current_time_santiago = datetime.now(santiago_tz)
    
    for index, row in df.iterrows():
        # Acceder a los datos de cada columna por nombre de columna
        name = row['Name']
        ip = row['IP']
        type_ = row['Type']
        parent_device = row['Parent Device']
        zone = row['Zone']



        if row['Last Time'] == 'never':
            last_time = pd.Timestamp('1900-01-01 00:00:00').tz_localize(santiago_tz)
        else:
            last_time = pd.to_datetime(row['Last Time'])

        datasource = name.split("-")[0].split("_")[0].split(" ")[0]

        if datasource not in ('Multicliente', 'TEST', 'Local'):

            company = Company.objects.filter(name = datasource)[0]

            log_source = LogSource.objects.get_or_create(
                name_log_source = name,
                ip = ip,
                company = company
            )[0]

            log_source.save()


            if (log_source.zona_horaria in "UTC"):
                utc = pytz.timezone('UTC')
                santiago = pytz.timezone('Chile/Continental')
                last_time = last_time.apply(lambda x: x.replace(tzinfo=utc).astimezone(santiago))
            else:
                # Si no está en UTC, al menos asegurarnos de que es tz-aware
                last_time = last_time.replace(tzinfo=santiago_tz)
                last_time = last_time - timedelta(hours=3)

            time_difference = (current_time_santiago - last_time).total_seconds() / 3600

            print(f"Fuente de dato: {name}. Ultimo evento: {last_time}. santiago: {current_time_santiago}. Time diference: {time_difference}")


            if time_difference > 2:

                registros_previos = RegistroHistorico.objects.filter(
                    name_log_source=log_source,
                    company=company,
                    estado=False
                )

                for registro in registros_previos:
                    registro.estado = True
                    registro.save()


                registro_historico = RegistroHistorico.objects.get_or_create(
                    timestamp           = last_time,
                    estado              = False,
                    escalado_a          = "Sin Gestión",
                    name_log_source     = log_source,
                    company             = company,
                )[0]

                registro_historico.save()

                # print(f"La diferencia de tiempo para {name} es de al menos 1 hora. Ultimo evento: {last_time}")


            else:
                # print(f"{name} Ultimo evento: {last_time}")

                registros_previos = RegistroHistorico.objects.filter(
                    name_log_source=log_source,
                    company=company,
                    estado=False
                )

                for registro in registros_previos:
                    registro.estado = True
                    registro.save()