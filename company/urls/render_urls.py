from company.views.render_views import CompanyTemplateView, ExampleTemplateView
from django.urls import path

urlpatterns = [
    path('', CompanyTemplateView.as_view(), name='company'),
    path('example', ExampleTemplateView.as_view(), name='example')
]

