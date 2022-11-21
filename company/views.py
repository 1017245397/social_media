from company.models import CompanyModel
from company.serializers import CompanySerializer
from rest_framework import viewsets


class CompanyViewSet(viewsets.ModelViewSet):
    '''API para companias'''
    queryset = CompanyModel.objects.all()
    serializer_class = CompanySerializer


