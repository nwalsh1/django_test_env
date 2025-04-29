from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request):
    #return HttpResponse("<h1> Hello World </h1>") #string of html code
    return render(request, 'home.html') #render the home.html template

def contact_view(request):
    return render(request, 'contact.html')

def about_view(request):
    return render(request, 'about.html')
