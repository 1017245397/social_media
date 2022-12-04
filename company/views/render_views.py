from django.views.generic.base import TemplateView


class CompanyTemplateView(TemplateView):
    template_name = "company.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context