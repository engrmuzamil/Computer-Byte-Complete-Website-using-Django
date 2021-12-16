from django import forms
from .models import Orders


class orderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['PhoneNo', 'Email' , 'DeliverAddress']
