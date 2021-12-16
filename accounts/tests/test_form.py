from django.test import SimpleTestCase
from accounts.forms import SignUpForm

class TestForms(SimpleTestCase):
    def test_form(self):
        form = SignUpForm(data={

             'first_name':'Muzamil ',
              'last_name':'Khan',
              'email':'engineer.muzamilkhan@gmail.com',
              
        })
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        form = SignUpForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),4)
