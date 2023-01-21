
from company.views.render_views import CompanyTemplateView, ProfileTemplateView,LoginTemplateView,\
    PublicationTemplateView,DetailsTemplateView
from django.urls import path

app_name='company'
urlpatterns = [
    path('register', CompanyTemplateView.as_view(), name='company'),
    path('profile', ProfileTemplateView.as_view(), name='profile'),
    path('login', LoginTemplateView.as_view(), name='login'),
    path('', PublicationTemplateView.as_view(), name='publication'),
    path('/<int:id>', PublicationTemplateView.as_view(), name='publication'),
    path('details', DetailsTemplateView.as_view(), name='details'),
    path('details/<int:id>', DetailsTemplateView.as_view(), name='details'),
]

