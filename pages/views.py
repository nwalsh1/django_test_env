from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request):
    #return HttpResponse("<h1> Hello World </h1>") #string of html code
    return render(request, 'home.html') #render the home.html template

def contact_view(request):
    
    return render(request, 'contact.html')

def about_view(request):
    my_context = {
        'title': 'This is my first django project',
        'my_number': 123,
        'my_list': [145, 223, 3325, 462],
        'my_html': '<h1> Hello World </h1>'
    }

    return render(request, 'about.html', my_context)

def social_view(request,*args, **kwargs):
    return HttpResponse("<h1>Social Page</h1>")
