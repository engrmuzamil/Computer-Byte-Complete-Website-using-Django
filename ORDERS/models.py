from django.db import models
from Store.models import Product
from django.contrib.auth.models import User
# Create your models here.
class Orders(models.Model):
    STATUS = (('New', 'New'), ('Completed', 'Completed'))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    orderID = models.CharField(max_length=20)
    Email = models.EmailField(max_length=50)
    PhoneNo = models.CharField(max_length=20)
    DeliverAddress = models.CharField(max_length=200)
    OrderTotal = models.FloatField()
    CreatedAt = models.DateTimeField(auto_now_add=True)
    UpdatedAt = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices = STATUS, default="New")

    def __str__(self):
        return self.orderID
class OrderDetail(models.Model):
    Order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    Products = models.ForeignKey(Product, on_delete=models.CASCADE)
    Qty = models.IntegerField()
    ProductPrice = models.FloatField()
    CreatedAt = models.DateTimeField(auto_now_add=True)
    UpdatedAt = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.Products.Product_Name
