from typing import Any, Dict
from django.views.generic.base import TemplateView
from company.forms import RegisterCompanyForm

class CompanyTemplateView(TemplateView):
    template_name: str = "company.html"
    
    def get_context_data(self) -> Dict[str, Any]:
        context: Dict[str, Any] = super().get_context_data()
        context['form_register_company'] = RegisterCompanyForm()
        return context


class LoginTemplateView(TemplateView):
    template_name: str = "login.html"

class PublicationTemplateView(TemplateView):
    template_name: str = "publication.html"

 
class ProfileTemplateView(TemplateView):
    template_name: str = "profile.html"

    def get_context_data(self, **kwargs) -> Dict[str, Any]:
        context: Dict[str, Any] = super().get_context_data()
        context["id"]=kwargs.get("id")
        return context

class DetailsTemplateView(TemplateView):
    template_name: str = "details.html"
    

    def get_context_data(self, **kwargs) -> Dict[str, Any]:
        context: Dict[str, Any] = super().get_context_data()
        context["id"]=kwargs.get("id")
        return context