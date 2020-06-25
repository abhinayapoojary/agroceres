"""agroceres URL Configuration

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
from django.urls import path
from agro_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', views.display, name='home'),
    path(r'selectstate/', views.select_state, name='selectstate'),
    path(r'selectdistrict/', views.select_district, name='selectdistrict'),
    path(r'area_under_growth/', views.area_under_growth, name='area_under_growth'),
    path(r'area_under_growth/<str:dist>', views.mandal, name='district'),
    path(r'select_mandal/', views.select_mandal, name='select_mandal'),

]
