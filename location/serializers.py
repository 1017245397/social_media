from rest_framework import serializers
from location.models import CountryModel, DeparmentModel, CityModel

class CountrySerializer(serializers.ModelSerializer):
    '''serializador de paises '''

    class Meta:
        model = CountryModel
        fields = '__all__'


class DeparmentSerializer(serializers.ModelSerializer):
    '''serializador de departamentos '''

    class Meta:
        model = DeparmentModel
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    '''serializador de ciudadess '''

    class Meta:
        model = CityModel
        fields = '__all__'