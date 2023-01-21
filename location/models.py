from django.db import models

# Create your models here.
class CountryModel(models.Model):
    """
    Modelo de paises
    """
    name = models.CharField("Nombre", max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Pais"
        verbose_name_plural="Paises"

class DeparmentModel(models.Model):
    """
    Modelo de departamentos
    """
    name = models.CharField("Nombre", max_length=150)
    country=models.ForeignKey(CountryModel, on_delete= models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Departamento"
        verbose_name_plural="Departamentos"

class CityModel(models.Model):
    """
    Modelo de ciudades
    """
    name = models.CharField("Nombre", max_length=150)
    department=models.ForeignKey(DeparmentModel, on_delete= models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Ciudad"
        verbose_name_plural="Ciudades"