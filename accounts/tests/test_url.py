from django.test import SimpleTestCase
from django.urls import reverse,resolve
from accounts.views import login_view, signup,logout_view

class TestUrls(SimpleTestCase):
    def test_signup(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func,signup)
    def test_login(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func,login_view)
    def test_logout(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func,logout_view)
