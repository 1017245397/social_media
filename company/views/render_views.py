from django.views.generic.base import TemplateView


class CompanyTemplateView(TemplateView):
    template_name = "company.html"

class ExampleTemplateView(TemplateView):
    template_name = "example.html"