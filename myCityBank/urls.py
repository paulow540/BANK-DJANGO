"""myCityBank URL Configuration

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
from re import template
from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('dashboard', TemplateView.as_view(template_name='dashboard.html'), name='dashboard'),
    path('contact', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('about', TemplateView.as_view(template_name='about.html'), name='about'),
    # path('login', TemplateView.as_view(template_name='login.html'), name='login'),


    re_path(r'^accounts/', include('django.contrib.auth.urls')),


]
