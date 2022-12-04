from company.models import CompanyModel, ContactCompanyModel,  CategoryCompanyModel, \
     GaleryCompanyModel , CommentCompanyModel
from company.serializers import CompanySerializer, ContactCompanySerializer, CategoryCompanySerializer, \
    GaleryCompanySerializer , CommentCompanySerializer
from rest_framework import viewsets


class CompanyViewSet(viewsets.ModelViewSet):
    '''API para companias'''
    queryset = CompanyModel.objects.all()
    serializer_class = CompanySerializer


class ContactCompanyViewSet(viewsets.ModelViewSet):
    '''API para contactos de la compania'''
    queryset = ContactCompanyModel.objects.all()
    serializer_class = ContactCompanySerializer


class CategoryCompanyViewSet(viewsets.ModelViewSet):
    '''API para categorias de las companias'''
    queryset = CategoryCompanyModel.objects.all()
    serializer_class = CategoryCompanySerializer


class GaleryCompanyViewSet(viewsets.ModelViewSet):
    '''API para galeria de la companias'''
    queryset = GaleryCompanyModel.objects.all()
    serializer_class = GaleryCompanySerializer


class CommentCompanyViewSet(viewsets.ModelViewSet):
    '''API para los comentarios de los usuarios para las companias'''
    queryset = CommentCompanyModel.objects.all()
    serializer_class = CommentCompanySerializer



