from typing import Any, List
from django.contrib import admin
from company.models import *
# Register your models here.

@admin.register(CompanyModel, 
CategoryCompanyModel, CommentCompanyModel, ContactCompanyModel, GaleryCompanyModel)
class UniversalAdmin(admin.ModelAdmin):
    
    def get_list_display(self, request) -> List[Any]:
        return [field.name for field in self.model._meta.concrete_fields]

    def get_list_filter(self, request) -> List[Any]:
        return [field.name for field in self.model._meta.concrete_fields]