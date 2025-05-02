from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import Product #import model
from .forms import ProductForm, RawProductForm #import form``

# Create your views here.
def product_detail_view(request):
    obj = Product.objects.get(id=1) #get the first product in the database
    # context = {
    #     'title': obj.title,
    #     'description': obj.description
    # }
    context = {
        'object': obj #pass the object to the template
    }
    return render(request, "products/product_detail.html", context)

# def product_create_view(request):
#     my_form = RawProductForm() #we create a form(GET)
#     if request.method == "POST": #check if the request is a POST request
#         my_form = RawProductForm(request.POST) 
#         if my_form.is_valid():
#             #now the data is good
#             #print(my_form.cleaned_data) #data from form after its been validated
#             Product.objects.create(**my_form.cleaned_data)#need ** to pass as arguements
#         else:
#             print(my_form.errors) #not valid print errors
#     context={
#         'form': my_form #pass the object to the template
#     }
#     return render(request, "products/product_create.html", context)

def product_create_view(request):
    initial_data = {
        'title' : 'My this awesome title'
    }
    obj = Product.objects.get(id=1)
    form = ProductForm(request.POST or None, instance=obj) #create a form instance with the data from the request
    if form.is_valid(): #check if the form is valid
        form.save() #save the form to the database
        form = ProductForm() #reset the form to an empty form

    context = {
        'form': form #pass the object to the template
    }
    return render(request, "products/product_create.html", context)

def dynamic_lookup_view(request,my_id): 
    #obj = Product.objects.get(id=my_id)
    #obj = get_object_or_404(Product, id=my_id)
    try:
        obj = Product.objects.get(id=my_id)
    except Product.DoesNotExist:
        raise Http404
    context = {
        "object" : obj
    }
    return render(request, "products/product_detail.html",context)