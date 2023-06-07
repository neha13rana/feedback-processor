"""
URL configuration for psc project.

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
from django.urls import path
from home import views
from home import utils

urlpatterns = [
    path('',views.index,name='home'),
    path('login',views.loginuser,name='login'),
    path('logout',views.logoutuser,name='logout'),
    path('safe1',views.safe1,name='safe1'),
    path('safe2',views.safe2,name='safe2'),
    path('check',views.check,name='check'),
    path('product1',views.pc1,name='product1'),
    path('product2',views.pc2,name='product2'),
    path('gp',views.graph,name="graph"),
    path('gp2',views.graph2,name="graph2"),
 
]
