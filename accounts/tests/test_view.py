from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.signup_url = reverse('register')
        self.logout_url = reverse('logout')
    def test_login(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'accounts/login.html')
    def test_signup(self):
        response = self.client.get(self.signup_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'accounts/register.html')
    def test_logout(self):
        response = self.client.get(self.logout_url)
        self.assertEquals(response.status_code,302)
        self.assertTemplateUsed(response,'/')
