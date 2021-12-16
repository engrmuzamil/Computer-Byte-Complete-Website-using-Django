from django.test import TestCase, Client
from django.urls import reverse
from CART.models import Cart,CartItems
from django.shortcuts import get_object_or_404
class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.cart_url = reverse('cart')
        self.checkout_url = reverse('checkout')
        self.add_cart_url = reverse('add_cart',kwargs={'product_id':3})
        self.remove_From_Cart_url = reverse('remove_From_Cart',args=[1])
        self.minus_From_Cart_url = reverse('minus_From_Cart',args=[1])


    def test_cart(self):
        response = self.client.get(self.cart_url )
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'cart.html')
    def test_checkout(self):
        response = self.client.get(self.checkout_url)
        self.assertEquals(response.status_code,302)
    def test_add_cart_url(self):
        response = self.client.get(self.add_cart_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'cart.html')
    def test_minus_From_Cart_url(self):
        response = self.client.get(self.minus_From_Cart_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'cart.html')
