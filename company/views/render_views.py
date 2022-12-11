from django.views.generic.base import TemplateView
from company.forms import CompanyForm, GaleryCompanyForm, CategoryCompanyForm, ContactCompanyForm
from user.forms import ProfileUserForm

class CompanyTemplateView(TemplateView):
    template_name = "company.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_company'] = CompanyForm()
        context['form_galery_company'] = GaleryCompanyForm()
        context['form_contact_company'] = ContactCompanyForm()
        context['form_category_company'] = CategoryCompanyForm()
        context['form_profile_user'] = ProfileUserForm()
        return context


class ExampleTemplateView(TemplateView):
    template_name = "example.html"