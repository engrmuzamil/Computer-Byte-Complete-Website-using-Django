from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Product, CATEGORY
from django.db.models import Q
# Create your views here.
def shop(request,CATEGORY_slug=None):
    categories = None
    product = None
    if CATEGORY_slug != None:
        categories = get_object_or_404(CATEGORY,slug = CATEGORY_slug)
        Products = Product.objects.filter(Product_Category = categories, is_available=True)
    else:
        Products = Product.objects.all().filter(is_available=True)
    context = {
            'Products' : Products,
        }
    return render(request, 'shop.html',context)

def productdetail(request,CATEGORY_slug, Product_Slug ):
    try:
        single_product = Product.objects.get( Product_Category__slug = CATEGORY_slug  ,Slug = Product_Slug)
    except Exception as e:
        raise e
    context = {
         'single_product' : single_product,
        }
    return render(request, 'productdetail.html',context)

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            Products= Product.objects.filter(Q(Product_Description__icontains=keyword) | Q(Product_Name__icontains=keyword))
            #Products = Product.objects.all().filter(is_available=True)
    context = {
            'Products' : Products,
        }
    return render(request, 'shop.html', context)