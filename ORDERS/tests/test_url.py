from django.test import SimpleTestCase
from django.urls import reverse,resolve
from ORDERS.views import placeOrder

class TestUrls(SimpleTestCase):
    def test_cart(self):
        url = reverse('placeOrder')
        self.assertEquals(resolve(url).func,placeOrder)
    
