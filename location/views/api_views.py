from location.models import CountryModel, DeparmentModel, CityModel
from location.serializers import CountrySerializer, DeparmentSerializer, CitySerializer
from rest_framework import viewsets
from django_filters import rest_framework as filters

class CountryViewSet(viewsets.ModelViewSet):
    '''API para paises'''
    queryset = CountryModel.objects.all()
    serializer_class = CountrySerializer


class DeparmentViewSet(viewsets.ModelViewSet):
    '''API para departamentos'''
    queryset = DeparmentModel.objects.all()
    serializer_class = DeparmentSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('country',)

class CityViewSet(viewsets.ModelViewSet):
    '''API para ciudades'''
    queryset = CityModel.objects.all()
    serializer_class = CitySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('department',)