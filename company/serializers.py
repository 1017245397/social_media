from rest_framework import serializers
from company.models import CompanyModel



class CompanySerializer(serializers.ModelSerializer):
    '''serializador de companias '''

    class Meta:
        model = CompanyModel
        fields = '__all__'

