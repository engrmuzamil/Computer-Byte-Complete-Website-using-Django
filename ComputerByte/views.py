from django.http import HttpResponse
from django.shortcuts import render
from Store.models import Product
def index(request):
    Products = Product.objects.all().filter(is_available=True)
    context = {
        'Products' : Products,

    }
    return render(request, 'index.html',context)
