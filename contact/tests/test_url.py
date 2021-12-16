from django.test import SimpleTestCase
from django.urls import reverse,resolve
from contact.views import contact_view
class TestUrls(SimpleTestCase):
    def test_contact(self):
        url = reverse('contact')
        self.assertEquals(resolve(url).func,contact_view)
