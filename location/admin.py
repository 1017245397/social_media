from django.contrib import admin
from location.models import *

@admin.register(DeparmentModel, CountryModel, CityModel)
class UniversalAdmin(admin.ModelAdmin):
    
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]
