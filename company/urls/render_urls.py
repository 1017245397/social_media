
from company.views.render_views import CompanyTemplateView, ProfileTemplateView,LoginTemplateView,PublicationTemplateView
from django.urls import path


urlpatterns = [
    path('', CompanyTemplateView.as_view(), name='company'),
    path('profile', ProfileTemplateView.as_view(), name='profile'),
    path('login', LoginTemplateView.as_view(), name='login'),
    path('publication', PublicationTemplateView.as_view(), name='publication')
]

