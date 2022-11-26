from rest_framework import serializers
from company.models import CompanyModel, ContactCompanyModel, CategoryCompanyModel , \
    GaleryCompanyModel , CommentCompanyModel

class CompanySerializer(serializers.ModelSerializer):
    '''serializador de companias '''

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




