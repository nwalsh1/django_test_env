from django.db import models

# Create your models here.
class Product(models.Model):
    title       = models.TextField()
    description = models.TextField()
    price       = models.TextField()
    summary     = models.TextField(default = 'this is a summary')


#when we make changes to the models.py, we need to run the following commands:
# python manage.py makemigrations
# python manage.py migrate