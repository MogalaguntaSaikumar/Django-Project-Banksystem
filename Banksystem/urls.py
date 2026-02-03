"""
URL configuration for Banksystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from Bank import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.admin_login, name='login'),
    path('menu/', views.admin_menu, name='admin_menu'),
    path('create/', views.create_account, name='create_account'),
    path('deposit/', views.deposit, name='deposit'),
    path('withdraw/', views.withdraw, name='withdraw'),
    path('balance/', views.balance, name='balance'),
    path('statement/', views.statement, name='statement'),
    path('logout/', views.logout, name='logout'),
]
