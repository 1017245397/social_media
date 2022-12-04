from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class CompanyModel(models.Model):
    '''
    Modelo de empresas
    '''
    nit=models.CharField("NIT", max_length=20, unique=True)
    description= models.TextField("Descripción", blank=True)
    mision=models.TextField("Misión", blank=True)
    vision=models.TextField("Visión", blank=True)
    name=models.CharField("Nombre", max_length=50)
    facebook=models.CharField("Facebook", max_length=150, blank=True)
    linkedin=models.CharField("linkedin", max_length=150, blank=True)
    instagram=models.CharField("Instagram", max_length=150, blank=True)
    twitter=models.CharField("Twitter", max_length=150, blank=True)
    web_site=models.CharField("Sitio Web", max_length=150, blank=True)

    class Meta:
        verbose_name="Empresa"
        verbose_name_plural="Empresas"
        

class ContactCompanyModel(models.Model):
    '''
    Modelo de información de contacto para las empresas
    '''
    address=models.CharField("Direccion", max_length=50, blank=True)
    cell_phone=models.CharField("Celular", max_length=10, blank=True)


    class Meta:
        verbose_name="Información de contacto para empresa"
        verbose_name_plural="Informacion de contacto para empresas"


class CategoryCompanyModel(models.Model):
    '''
    Modelo de categorias de las compañias
    '''
    name=models.CharField("Nombre", max_length=150 )
    description= models.TextField("Descripción", max_length=450)
    companies=models.ManyToManyField(CompanyModel)

    class Meta:
        verbose_name="Categoria de la empresa"
        verbose_name_plural="Categorias de las empresas"

    
class GaleryCompanyModel(models.Model):
    '''
    Modelo galeria de fotos de la compañia
    '''
    photo=models.FileField(upload_to='company')
    company=models.ForeignKey(CompanyModel, on_delete= models.CASCADE)

    class Meta:
        verbose_name="Galeria de la compañia"
        verbose_name_plural="Galerias de las compañias"


class CommentCompanyModel(models.Model):
    '''
    Modelo de comentarios
    '''
    comment=models.TextField("Comentarios", max_length=500)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name="Comentario de usuario a empresa"
        verbose_name="Comentarios de usuarios a empresas"

    
