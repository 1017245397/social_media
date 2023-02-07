from typing import Any, OrderedDict
from rest_framework import serializers
from company.models import CompanyModel, ContactCompanyModel, CategoryCompanyModel , \
    GaleryCompanyModel , CommentCompanyModel
from user.models import ProfileUserModel

class CompanySerializer(serializers.ModelSerializer):
    '''serializador de companias '''

    def to_representation(self, instance: CompanyModel)-> Any:
        representation: OrderedDict[Any, Any] = super().to_representation(instance)
        representation["country"] = instance.country.name
        representation["deparment"] = instance.deparment.name
        representation["city"] = instance.city.name
        try:
            profile = ProfileUserModel.objects.get(user=instance.user)
            representation["names"] = f"{profile.first_names} {profile.last_names}"
            representation["phone"] = profile.phone_number
        except ProfileUserModel.DoesNotExist:
            pass

        return representation

    class Meta:
        model = CompanyModel
        fields = '__all__'
         

class ContactCompanySerializer(serializers.ModelSerializer):
    '''serializador de contacto de companias '''

    class Meta:
        model = ContactCompanyModel
        fields = '__all__'


class CategoryCompanySerializer(serializers.ModelSerializer):
    '''serializador de categorias de companias '''

    class Meta:
        model = CategoryCompanyModel
        fields = '__all__'


class GaleryCompanySerializer(serializers.ModelSerializer):
    '''serializador de galeria de companias '''

    class Meta:
        model = GaleryCompanyModel
        fields = '__all__'


class CommentCompanySerializer(serializers.ModelSerializer):
    '''serializador de comentarios del usuario'''

    class Meta:
        model = CommentCompanyModel
        fields = '__all__'




