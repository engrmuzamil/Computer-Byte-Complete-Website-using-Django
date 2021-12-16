from django.test import SimpleTestCase
from django.urls import reverse,resolve
from Store.views import shop, productdetail, search

class TestUrls(SimpleTestCase):
    def test_shop(self):
        url = reverse('shop')
        self.assertEquals(resolve(url).func,shop)
    def test_productdetail(self):
        url = reverse('productdetail',args=["new", "new2"])
        self.assertEquals(resolve(url).func,productdetail)
    def test_search(self):
        url = reverse('search')
        self.assertEquals(resolve(url).func,search)
    def test_cat(self):
        url = reverse('shop', args=["new"])
        self.assertEquals(resolve(url).func,shop)
