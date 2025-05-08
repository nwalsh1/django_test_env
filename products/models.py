from django.db import models
from django.urls import reverse
# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=120) #max_length required
    description = models.TextField(blank=True,null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=10000) 
    summary     = models.TextField(blank=False,null=False) 
    #blank - field that is rendereed, null- database
    featured    = models.BooleanField(default=True) # null=True or default =True

    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"my_id": self.id}) 
    #reverse is used to get the url of the product detail view
    #products: is the namespace of the app, product-detail is the name of the url
