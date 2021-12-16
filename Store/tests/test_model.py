from django.test import TestCase
from CART.models import Cart,CartItems
from Categories.models import CATEGORY
from Store.models import Product
class TestModels(TestCase):
    def setUp(self):
        self.cat = CATEGORY.objects.create(
            Category_Name= "RANDOM NAME FOR CAT",
            slug = "RANDOM-NAME-FOR-CAT"
        )
        self.product = Product.objects.create(
            Product_Name = "Mouse",
            Product_Price = 100,
            Product_Qty = 1000,
            Product_Category = self.cat,
        )
    def test_product(self):
        self.assertEquals(self.product.Product_Name, "Mouse" )
