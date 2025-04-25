from django.contrib import admin

# Register your models here.
from .models import Product #relative import, from the same directory
admin.site.register(Product) #register the Product model with the admin site