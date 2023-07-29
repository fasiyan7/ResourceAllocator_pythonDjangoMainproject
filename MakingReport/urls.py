"""Oneteamallocator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from . import views
app_name = 'MakingReport'
urlpatterns = [
    # this url applied in students'viewmarklist. actually this code wanted for staff marklist. it shows all student marklist. student want their marklist only so that to pass id to the method
    path('marklist/',views.marklist_view, name='marklist'),
    path('pdf/', views.pdf_view, name='pdf'),
]
path('MakingReport/', include('MakingReport.urls')),
