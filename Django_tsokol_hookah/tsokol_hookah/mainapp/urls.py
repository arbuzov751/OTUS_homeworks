"""tsokol_hookah URL Configuration

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
from django.urls import path
import mainapp.views as mainapp
import menu.views as menu
from django.views.generic import TemplateView

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.mainpage, name='mainpage'),
    path('menu/', menu.MenuListView.as_view(), name='menu_list'),
    # path('about/', mainapp.about, name='about'),
    path('about/', TemplateView.as_view(template_name='mainapp/about.html'), name='about'),
]
