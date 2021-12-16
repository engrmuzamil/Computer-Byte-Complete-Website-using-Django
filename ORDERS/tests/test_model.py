from django.test import TestCase
from ORDERS.models import Orders,OrderDetail
from Store.models import Product
from Categories.models import CATEGORY
from django.contrib.auth.models import User
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
        self.user = User.objects.create(
         username = "GeneralUser",
         password = "MyComplexPass1122_",
         email = "LetsCreateEmail@gmail.com"
        )
        self.order = Orders.objects.create(
            user= self.user,
            orderID = "12323123skjdskd",
            Email = "LetsCreateEmail@gmail.com",
            PhoneNo = "1232131",
            DeliverAddress = "Mardan",
            OrderTotal = 12000,
            status = "NEW"
        )
        self.orderdetail = OrderDetail.objects.create(
            Order = self.order,
            Products = self.product,
            Qty = 21,
            ProductPrice = 100
        )
    def test_Order(self):
        self.assertEquals(self.order.orderID, "12323123skjdskd" )
    def test_CartItems(self):
        self.assertEquals(self.orderdetail.Products.Product_Name,self.product.Product_Name)
