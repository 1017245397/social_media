from django.db import models

# Create your models here.
class CompanyModel(models.Model):
    '''
    Modelo de empresas
    '''
    nit=models.CharField(max_length=20,unique=True,verbose_name="nit")
    description= models.TextField(verbose_name="descripcion", blank=True)
    mision=models.TextField("mision",blank=True)
    vision=models.TextField("vision",blank=True)
    name= models.CharField("nombre",max_length=50)

    class Meta:
        verbose_name="empresa"
        verbose_name_plural="empresas"
        


