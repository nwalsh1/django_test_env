from django.contrib import admin

# Register your models here.
from .models import Article #relative import

admin.site.register (Article)