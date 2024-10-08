"""
URL configuration for evaluacionSumativa1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from item1App.views import index, dic_num, dic_log, dic_hib

urlpatterns = [
    path('admin/', admin.site.urls),
    path('item1/index/', index),
    path('item2/numerico/', dic_num),
    path('item2/logico', dic_log),
    path('item2/hibrido', dic_hib)
]
