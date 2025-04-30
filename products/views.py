from django.shortcuts import render

from .models import Product #import model

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
    return render(request, "product/detail.html", context)