from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from CART.views import _cart_id
from CART.models import CartItems, Cart
# Create your views here.

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            try:
                cart = Cart.objects.get(Cart_ID=_cart_id(request))
                itemExistInCart = CartItems.objects.filter(cart=cart).exists()
                print(itemExistInCart)
                if itemExistInCart:
                    cart_item = CartItems.objects.filter(cart=cart)
                    for item in cart_item:
                        item.user = user
                        item.save()

            except:
                pass
            login(request, user)

            return redirect('/')
    return render(request, 'accounts/login.html')

def logout_view(request):
    if request.user.is_authenticated:
         return HttpResponse(render(request, 'accounts/login.html'), logout(request))
    else:
        return redirect('/')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})
