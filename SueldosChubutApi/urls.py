"""
URL configuration for SueldosChubutApi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.shortcuts import redirect
from django.views.generic import RedirectView
from api import urls as api_urls
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

API_VERSION = 'v2'

urlpatterns = [
    path('admin/', admin.site.urls),
    path(f'api/{API_VERSION}/', include(api_urls)),
    path(f'api/{API_VERSION}/schema/', SpectacularAPIView.as_view(), name="schema"),
    path(f'api/{API_VERSION}/schema/docs', SpectacularSwaggerView.as_view(url_name="schema")),
    #path('', RedirectView.as_view(url='api/v1/')),
    path('', lambda request: redirect(f'api/{API_VERSION}/', permanent=True)),
]

