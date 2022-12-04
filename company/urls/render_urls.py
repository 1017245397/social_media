from company.views.render_views import CompanyTemplateView
from django.urls import path

urlpatterns = [
    path('', CompanyTemplateView.as_view(),name='company')
    ]

