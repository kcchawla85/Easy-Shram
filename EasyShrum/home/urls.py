"""EasyShrum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('user-login/', views.ulogin),
    path('user-login/create-user', views.createuser),
    path('admin-login/', views.alogin),
    path('admin-login/create-admin', views.createadmin),
    path('user-job-form/', views.userjobform),
    path('user-form/', views.userjobform),
    path('post-a-job/', views.postjob),
]
