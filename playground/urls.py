#map urls to views
from django.urls import path
from . import views #to reference views

app_name = 'playground'
#url configurations
urlpatterns = [
    path('hello/',views.say_hello,name = "hello"), #this is the url we will use to access this view
]