from django.urls import path
from . import views
urlpatterns = [
    path('', views.cart, name = 'cart'),
    path('add_cart/<int:product_id>/', views.add_cart, name = 'add_cart'),
    path('remove_From_Cart/<int:product_id>/', views.remove_From_Cart, name = 'remove_From_Cart'),
    path('minus_From_Cart/<int:product_id>/', views.minus_From_Cart, name = 'minus_From_Cart'),
    path('checkout/', views.checkout, name = 'checkout'),
]
