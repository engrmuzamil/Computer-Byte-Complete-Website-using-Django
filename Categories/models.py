from django.db import models
from django.urls import reverse
# Create your models here.
class CATEGORY(models.Model):
    Category_Name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(max_length=200,unique=True)
    def __str__(self):
        return self.Category_Name
    def get_url(self):
        return reverse('shop', args = [self.slug])
