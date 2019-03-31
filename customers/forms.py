from django import forms
from. import models



class CustomerForm(forms.ModelForm):
    class Meta:
        model= models.Customers
        fields=['cust_name','cust_age','cust_address','cust_phone_number']

