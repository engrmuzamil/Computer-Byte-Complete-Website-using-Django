from django.shortcuts import render, redirect, get_object_or_404
from Store.models import Product
from .models import Cart, CartItems
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
# Create your views here.
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart
def add_cart(request,product_id):
    product = get_object_or_404(Product, id = product_id)
    if product.Product_Qty <= 0:
        return redirect('cart')
    else:
            if request.user.is_authenticated:
                try:
                    cart = Cart.objects.get(Cart_ID = _cart_id(request))
                except Cart.DoesNotExist:
                    cart = Cart.objects.create(
                    Cart_ID = _cart_id(request)
                    )
                    cart.save()
                try:
                    cart_item = CartItems.objects.get(user=request.user,product=product, cart = cart)
                    cart_item.Quantity += 1
                    cart_item.save()
                except CartItems.DoesNotExist:
                    cart_item = CartItems.objects.create(
                    user = request.user,
                    product = product,
                    Quantity = 1,
                    cart = cart,
                    )
                    cart_item.save()
            else:
                try:
                    cart = Cart.objects.get(Cart_ID = _cart_id(request))
                except Cart.DoesNotExist:
                    cart = Cart.objects.create(
                    Cart_ID = _cart_id(request)
                    )
                    cart.save()
                try:
                    cart_item = CartItems.objects.get(product=product, cart=cart)
                    cart_item.Quantity += 1
                    cart_item.save()
                except CartItems.DoesNotExist:
                    cart_item = CartItems.objects.create(
                    product = product,
                    Quantity = 1,
                    cart = cart,
                    )
                    cart_item.save()
            return redirect('cart')

def remove_From_Cart(request, product_id):

    product = get_object_or_404(Product, id = product_id)
    if request.user.is_authenticated:
        cart_item = CartItems.objects.get(user=request.user,product=product)
    else:
        cart = Cart.objects.get(Cart_ID = _cart_id(request))
        cart_item = CartItems.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart')

def minus_From_Cart(request, product_id):

    product = get_object_or_404(Product, id = product_id)
    if request.user.is_authenticated:
        cart_item = CartItems.objects.get(user=request.user,product=product)
    else:
        cart = Cart.objects.get(Cart_ID = _cart_id(request))
        cart_item = CartItems.objects.get(product=product, cart=cart)
    if cart_item.Quantity > 1:
        cart_item.Quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')

def cart(request, total=0, quantity=0, cart_items=None):
    try:
        if request.user.is_authenticated:
            cart_items = CartItems.objects.filter(user=request.user,IsActive=True)
        else:
            cart = Cart.objects.get(Cart_ID =_cart_id(request))
            cart_items = CartItems.objects.filter(cart=cart,IsActive=True)
        for cart_item in cart_items:
            total  +=  (cart_item.product.Product_Price * cart_item.Quantity)
            quantity += cart_item.Quantity
    except ObjectDoesNotExist:
        pass
    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,

    }
    return render(request, 'cart.html',context)


@login_required(login_url="login")
def checkout(request, total=0, quantity=0, cart_items=None):
        try:
            cart = Cart.objects.get(Cart_ID =_cart_id(request))
            cart_items = CartItems.objects.filter(cart=cart,IsActive=True)
            for cart_item in cart_items:
                total  +=  (cart_item.product.Product_Price * cart_item.Quantity)
                quantity += cart_item.Quantity
        except ObjectDoesNotExist:
            pass
        context = {
            'total': total,
        }
        return render(request, 'checkout.html',context)
