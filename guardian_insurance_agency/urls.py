"""guardian_insurance_agency URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from pages.views import (
    HomeView,
    PersonalView,
    CommercialView,
    ContactView,
    AboutView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('personal/', PersonalView.as_view(), name='personal'),
    path('commercial/', CommercialView.as_view(), name='commercial'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about'),
    path('blog/', include('articles.urls')),
    path('staff/', include('staff.urls')),
    path('admin/', admin.site.urls),
]
