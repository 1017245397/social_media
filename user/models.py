from django.db import models
from django.contrib.auth.models import User
from user.globals import TYPE_DOCUMENT_CHOICES, CIVIL_ESTATUS_CHOICES, GENDER_CHOICES




# Create your models here.
class ProfileUserModel(models.Model):
    '''Modelo del Usuario'''
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    type_document=models.CharField("Tipo de Documento", max_length=10, choices = TYPE_DOCUMENT_CHOICES)
    document=models.CharField("Numero de Identificación", max_length=20, unique=True)
    first_names= models.CharField("Nombres", max_length= 150)
    last_names=models.CharField("Apellidos", max_length=150)
    birthdate=models.DateField("Fecha de Nacimiento")
    civil_status=models.CharField("Estado Civil", max_length=20, choices = CIVIL_ESTATUS_CHOICES)
    gender=models.CharField("Genero", max_length=10, choices = GENDER_CHOICES)
    phone_number=models.CharField("Numero de telefono", max_length=15)
    email=models.CharField("Correo", max_length=50)
    
    class Meta:
        verbose_name="Perfil de usuario"
        verbose_name_plural="Perfiles de usuarios"




    
