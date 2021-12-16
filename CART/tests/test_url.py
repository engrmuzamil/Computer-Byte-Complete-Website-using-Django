from django.test import SimpleTestCase
from django.urls import reverse,resolve
from CART.views import add_cart, remove_From_Cart, cart, minus_From_Cart, checkout

class TestUrls(SimpleTestCase):
    def test_cart(self):
        url = reverse('cart')
        self.assertEquals(resolve(url).func,cart)
    def test_checkout(self):
        url = reverse('checkout')
        self.assertEquals(resolve(url).func,checkout)
    def test_add_cart(self):
        url = reverse('add_cart',args=[1])
        self.assertEquals(resolve(url).func,add_cart)
    def test_remove_From_Cart(self):
        url = reverse('remove_From_Cart', args=[1])
        self.assertEquals(resolve(url).func,remove_From_Cart)
    def test_minus_From_Cart(self):
        url = reverse('minus_From_Cart', args=[1])
        self.assertEquals(resolve(url).func,minus_From_Cart)
