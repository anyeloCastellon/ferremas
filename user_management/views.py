from cgitb import enable
from django.shortcuts import render
from requests import delete

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_204_NO_CONTENT
from base.views import GeneralModelView


from user_management.models import Company, TypeCompany
from user_management.serializers import CompanyModelSerializerMinumus, TypeCompanyModelSerializerMinumus


class CompanyViewSet(GeneralModelView):
    queryset = Company.objects.all()
    serializer_class = CompanyModelSerializerMinumus
    
    def perform_create(self, serializer):
        serializer.save(
            type_company_id=self.request.data['type_company']['id']
        )

class TypeCompanyViewSet(GeneralModelView):
    queryset = TypeCompany.objects.all()
    serializer_class = TypeCompanyModelSerializerMinumus
