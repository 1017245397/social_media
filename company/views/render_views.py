from django.views.generic.base import TemplateView
from company.forms import RegisterCompanyForm

from user.forms import ProfileUserForm

class CompanyTemplateView(TemplateView):
    template_name = "company.html"
    
    def get_context_data(self):
        context = super().get_context_data()
        context['form_register_company'] = RegisterCompanyForm()
        
        return context



class ExampleTemplateView(TemplateView):
    template_name = "example.html"
    

