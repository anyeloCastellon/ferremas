from user_management.models import User, Company, TypeCompany
from rest_framework import serializers


class CompanyHyperlinkedModelSerializerMinumus(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ['id_company', 'name', 'enabled']


class CompanyModelSerializerMinumus(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id_company', 'name', 'enabled']

class CompanyModelSerializerMaxMinumus(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name',]


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class TypeCompanyModelSerializerMinumus(serializers.ModelSerializer):
    class Meta:
        model = TypeCompany
        fields = ['id', 'name', 'description', 'enabled']


