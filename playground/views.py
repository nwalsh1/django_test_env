from django.shortcuts import render
from django.http import HttpResponse #allows us to return a response to the user

# Create your views here.
# request handler
# action - pull data from DB, send email etc

# request -> response
def say_hello(request): 
    x=1
    y=2
    z=x+y
    #return HttpResponse('Hello World!') #prints hello world to screen
    return render(request, 'hello.html',{'name':'Neil'}) #render the hello.html template
#need to map this view to an url so when we get a request this will be called

