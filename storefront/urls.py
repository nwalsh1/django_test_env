"""
URL configuration for storefront project.

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
from django.urls import path, include
import debug_toolbar

from pages.views import home_view, contact_view, about_view
from products.views import (
    product_detail_view, 
    product_create_view,
    dynamic_lookup_view
    )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    #pages urls
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    #products urls
    path('product/', product_detail_view, name='product'),
    path('create/', product_create_view, name='create'),
    path('products/<int:my_id>/', dynamic_lookup_view, name='products'),

    path('playground/', include('playground.urls')), 
    path('__debug__/', include(debug_toolbar.urls)) #add this line to the urls.py file to include the debug toolbar urls
    #send all urls that start with playground to the urls.py file in the playground app
]

