from django.test import TestCase
from CART.models import Cart,CartItems
from django.shortcuts import  get_object_or_404
from Store.models import Product
class TestModels(TestCase):
    def setUp(self):
        self.cart = Cart.objects.create(
            Cart_ID= "RANDOM ID FOR CART"
        )
        self.cartitem = CartItems.objects.create(
            cart = self.cart,
            Quantity = 10,
            product = get_object_or_404(Product, Slug = "hpkeyboardwired")
        )
    def test_Cart(self):
        self.assertEquals(self.cart.Cart_ID, "RANDOM ID FOR CART" )
    def test_CartItems(self):
        self.assertEquals(self.cartitem.cart.Cart_ID,"RANDOM ID FOR CART")
