from django.test import TestCase
from contact.models import Contact
class TestModels(TestCase):
    def setUp(self):
        self.Contact = Contact.objects.create(
            email= "muzamil@gmail.com",
            subject="Any Query",
            message="iahdssajdsjdsahdjs"
        )
    def test_Contact(self):
        self.assertEquals(self.Contact.subject, "Any Query" )
