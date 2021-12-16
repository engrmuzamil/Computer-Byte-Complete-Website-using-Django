from django.db import models
from Store.models import Product
from django.contrib.auth.models import User
# Create your models here.
class Cart(models.Model):
    Cart_ID = models.CharField(max_length=250, blank = True)
    Date_Added = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.Cart_ID

class CartItems(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete= models.CASCADE, null=True)
    Quantity = models.IntegerField()
    IsActive = models.BooleanField(default = True)

    def sub_total(self):
        return self.product.Product_Price * self.Quantity
    def __str__(self):
        return self.product.Product_Name;
