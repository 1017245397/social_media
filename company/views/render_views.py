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
    
    def get_context_data(self) -> Dict[str, Any]:
        context: Dict[str, Any] = super().get_context_data()
        context['x'] = range(12)
        return context



class ProfileTemplateView(TemplateView):
    template_name: str = "profile.html"


class DetailsTemplateView(TemplateView):
    template_name: str = "details.html"
    

