from django.db import models
from django.urls import reverse #for redirecting to the article page after creating it

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=120) #max_length required
    content = models.TextField(blank=True,null=True)
    active = models.BooleanField(default=True) #blank - field that is rendereed, null- database

    def get_absolute_url(self):
        return reverse("articles:article-detail", kwargs={"id": self.id})
    