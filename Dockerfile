# syntax=docker/dockerfile:1
FROM python:3.9
ENV PYTHONUNBUFFERED=1

ARG ATN_PROD
ENV ATN_PROD=$ATN_PROD

ARG ATN_DB_ENGINE
ENV ATN_DB_ENGINE=$ATN_DB_ENGINE

ARG ATN_DB
ENV ATN_DB=$ATN_DB

ARG ATN_DB_USER
ENV ATN_DB_USER=$ATN_DB_USER

ARG ATN_DB_HOST
ENV ATN_DB_HOST=$ATN_DB_HOST

ARG ATN_DB_PORT
ENV ATN_DB_PORT=$ATN_DB_PORT

ARG ATN_DB_PASSWD
ENV ATN_DB_PASSWD=$ATN_DB_PASSWD

RUN apt-get update && apt install -y libpq-dev python3-dev gcc g++  && apt-get -y install cron  && touch /var/log/cron.log
RUN mkdir /home/logs && touch /home/logs/logs.log && touch /home/logs/logs.criticidad.log && touch /home/logs/logs_eps_qradar.log && touch /home/logs/logs_eps_mcafee.log
RUN printenv | grep -v "no_proxy" >> /etc/environment

RUN mkdir /etc/nginx
RUN mkdir /etc/nginx/cert

WORKDIR /code
RUN mkdir logs
RUN touch logs/gunicorn.error.log
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/


CMD ["gunicorn", "-c", "config/gunicorn/conf.py", "--bind", ":8000", "--timeout", "13000",  "eps.wsgi:application"]