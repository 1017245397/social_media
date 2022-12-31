from typing import Any, Dict
from django.views.generic.base import TemplateView
from company.forms import RegisterCompanyForm

class CompanyTemplateView(TemplateView):
    template_name: str = "company.html"
    
    def get_context_data(self) -> Dict[str, Any]:
        context: Dict[str, Any] = super().get_context_data()
        context['form_register_company'] = RegisterCompanyForm()
        return context


class ExampleTemplateView(TemplateView):
    template_name: str = "example.html"
    

