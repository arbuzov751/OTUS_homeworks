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

app_name = 'menu'

urlpatterns = [
    # path('menu/', menu.menu_list, name='menu_list'),
    path('', menu.MenuListView.as_view(), name='menu_list'),
    path('detail/<int:pk>/', menu.MenuListDetailView.as_view(), name='menu_detail'),
]
