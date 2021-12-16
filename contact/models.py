from django.db import models
from django.urls import reverse
# Create your models here.

class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email
    def get_url(self):
        return reverse('contact')
