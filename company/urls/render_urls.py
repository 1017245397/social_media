
from company.views.render_views import ProfileTemplateView,LoginTemplateView,\
    PublicationTemplateView,DetailsTemplateView
from django.urls import path

app_name='company'
urlpatterns = [
    path('register/', ProfileTemplateView.as_view(), name='profile'),
    path('profile/<int:id>', ProfileTemplateView.as_view(), name='profile'),
    path('login/', LoginTemplateView.as_view(), name='login'),
    path('', PublicationTemplateView.as_view(), name='publication'),
    path('details/', DetailsTemplateView.as_view(), name='details'),
    path('details/<int:id>', DetailsTemplateView.as_view(), name='details'),
]

