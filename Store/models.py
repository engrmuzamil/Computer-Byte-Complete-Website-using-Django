from django.db import models
from Categories.models import CATEGORY
from django.urls import reverse
# Create your models here.
class Product(models.Model):
    Product_Name = models.CharField(max_length=200,unique=True)
    Slug = models.SlugField(max_length=200,unique=True)
    Product_Description = models.TextField(max_length=500,blank=True)
    Product_Image = models.ImageField(upload_to='photos/Products')
    Product_Qty = models.IntegerField()
    Product_Price = models.IntegerField()
    Product_Category = models.ForeignKey(CATEGORY, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)
    Created_Date = models.DateTimeField(auto_now_add=True)
    Updated_Date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Product_Name
    def get_url(self):
        return reverse('productdetail', args = [self.Product_Category.slug, self.Slug])
