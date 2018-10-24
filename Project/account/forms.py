from django import forms
from dataimport.models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Customers 
		fields= '__all__'
		widgets = {
			'customer_birthday' : forms.DateInput(attrs={'type': 'date'}),

		}

		labels = {
            'customer_name': "Your Full Name",
            'customer_phone': "Your Phone Number",
            'customer_address': "Your Address",
            'customer_birthday': "Date of Birth",
            'customer_occupation': "Your Occupation",
            'customer_gender': "Gender",
        }

		