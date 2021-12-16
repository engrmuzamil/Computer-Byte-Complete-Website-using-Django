from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(
         username = "GeneralUser",
         password = "MyComplexPass1122_",
         email = "LetsCreateEmail@gmail.com"
        )
        self.placeOrder_url = reverse('placeOrder')
    def test_placeOrder(self):
        response = self.client.get(self.placeOrder_url )
        self.assertEquals(response.status_code,302)
