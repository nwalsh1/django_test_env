from django.db import models

# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=120) #max_length required
    description = models.TextField(blank=True,null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=8) 
    summary     = models.TextField()


#when we make changes to the models.py, we need to run the following commands:
# python manage.py makemigrations
# python manage.py migrate