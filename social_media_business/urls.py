"""social_media_business URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from user.views.api_views import LoginView, my_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-company/', include('company.urls.api_urls')),
    path('api-location/', include('location.urls.api_urls')),
    path('api-user/', include('user.urls.api_urls')),
    path('', include('company.urls.render_urls', namespace='company')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('login-auth/', LoginView.as_view(), name='login-auth'),
    path('logout/', my_logout, name='logout'),
]

