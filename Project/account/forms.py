from django import forms
from dataimport.models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Customers 
		fields = '__all__'
		widgets = {
			'customer_birthday' : forms.DateInput(attrs={'type': 'date'}),

		}

		labels = {
            'order_id': "Order ID",
            'customer_name': "Your Full Name",
            'customer_phone': "Your Phone Number",
            'customer_address': "Your Address",
            'customer_birthday': "Date of Birth",
            'customer_occupation': "Your Occupation",
            'customer_gender': "Gender",
            'order_car' : "Car Name"
        }

	def __init__(self, *args, **kwargs):
	    super(ProfileForm, self).__init__(*args, **kwargs)
	    self.helper = FormHelper()
	    self.helper.form_tag = True
	    self.helper.form_class = 'form-horizontal'
	    self.helper.label_class = 'col-sm-3'
	    self.helper.field_class = 'col-sm-9'
	    self.helper.add_input(Submit('submit', 'Submit'))
		