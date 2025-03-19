"""taxi URL Configuration

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
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('admin/', admin.site.urls),
    path('make_order/', views.make_order, name='make_order'),
    path('clients/', views.client_list, name='client_list'),
    path('drivers/', views.driver_list, name='driver_list'),
    path('orders/', views.order_list, name='order_list'),
    path('clients/<int:id>', views.client_detail, name='client_detail'),
    path('orders/<int:id>', views.order_detail, name='order_detail'),
    path('drivers/<int:id>', views.driver_detail, name='driver_detail')
]
