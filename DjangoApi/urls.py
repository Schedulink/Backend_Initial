"""
URL configuration for DjangoApi project.

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
from django.urls import path,include
# from ttgapp import urls as dept_urls
from django.contrib.auth import views as auth_views
from ttgapp.views import adminview
from rest_framework import routers

route=routers.DefaultRouter()
route.register("",adminview,basename="adminview")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ttgapp/',include(route.urls))
    # path('ttgapp/',include('ttgapp.urls')),
]

