"""authProject URL Configuration

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
from django.contrib import admin
from django.urls import path
from authApp.login import login
from authApp.views.market.create import create_market
from authApp.views.customer.create import create_customer
from authApp.views.users.create import create



urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login),
    path('market/create', create_market),
    path('customers/create', create_customer),
    path('users/list', create.as_view({'get':'list'})),
   
]