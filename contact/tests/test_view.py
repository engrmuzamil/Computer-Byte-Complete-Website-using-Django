from django.test import TestCase, Client
from django.urls import reverse
from contact.views import contact_view
class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.contact_view_url = reverse('contact')

    def test_contact(self):
        response = self.client.get(self.contact_view_url )
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'contact.html')
