from django.shortcuts import render, redirect,  HttpResponse
from CART.models import CartItems
from .forms import orderForm
from django import forms
import datetime
from .models import Orders, OrderDetail
from django.core.mail import send_mail
from Store.models import Product
from django.contrib.auth.decorators import login_required

@login_required
def placeOrder(request):
    currentUser = request.user
    cartItem = CartItems.objects.filter(user = currentUser)
    cartCount = cartItem.count()
    if cartCount <= 0:
        return redirect('shop')
    total = 0
    cart_items = CartItems.objects.filter(user=request.user,IsActive=True)
    for cart_item in cart_items:
        total  +=  (cart_item.product.Product_Price * cart_item.Quantity)
    form = orderForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        print("Come Here")
        data = Orders()
        data.user = currentUser
        data.Email = form.cleaned_data['Email']
        data.PhoneNo = form.cleaned_data['PhoneNo']
        data.DeliverAddress = form.cleaned_data['DeliverAddress']
        data.OrderTotal = total
        data.save()
        yr = int(datetime.date.today().strftime('%Y'))
        dt = int(datetime.date.today().strftime('%d'))
        mo = int(datetime.date.today().strftime('%m'))
        d = datetime.date(yr,mo,dt)
        currDate = d.strftime("%Y%m%d")
        ip = request.META.get('REMOTE_ADDR')
        orderID = currDate + str(ip) + str(data.id)
        data.orderID = orderID
        data.save()

        cart_item1 = CartItems.objects.filter(user=request.user)
        for cart_item in cart_item1:
            orderprod = OrderDetail()
            orderprod.Qty = cart_item.Quantity
            orderprod.Products = cart_item.product
            orderprod.Order = data
            orderprod.ProductPrice = cart_item.product.Product_Price
            orderprod.save()

            product = Product.objects.get(id=cart_item.product.id)
            product.Product_Qty -= cart_item.Quantity
            product.save()
        CartItems.objects.filter(user=request.user).delete()
        return HttpResponse("Order is Created Successfully")
