from django.test import TestCase, Client
from django.urls import reverse
from Store.models import Product
class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.shop_url = reverse('shop')
        self.productdetail_url = reverse('productdetail',args=["Keyboard", "hpkeyboardwired"])
        self.search_url =  reverse('search')
        self.cat_url = reverse('shop', args=["Keyboard"])
    def test_shop(self):
        response = self.client.get(self.shop_url )
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'shop.html')
    def test_productdetail(self):
        response = self.client.get(self.productdetail_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'productdetail.html')
    def test_search(self):
        response = self.client.get(self.search_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'shop.html')
    def test_cat_url(self):
        response = self.client.get(self.cat_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'shop.html')
