from cgitb import enable
from django.shortcuts import render
from requests import delete

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_204_NO_CONTENT
from base.views import GeneralModelView

