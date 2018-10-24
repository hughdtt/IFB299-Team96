from django import forms
from dataimport.models import *
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class ReserveForm(forms.ModelForm):
	class Meta:
		model = Orders
		fields = '__all__'
		widgets = {
			'order_createdate' : forms.DateInput(attrs={'type': 'date'}),
			'order_pickupdate' : forms.DateInput(attrs={'type': 'date'}),
			'order_returndate' : forms.DateInput(attrs={'type': 'date'}),
			'order_car' : forms.HiddenInput(),
			'order_customer' : forms.HiddenInput(),
			'order_status' : forms.HiddenInput(),


		}

		labels = {
            'order_id': "Order ID",
            'order_createdate': "Date Created",
            'order_pickupdate': "Pickup Date",
            'order_returndate': "Return Date",
            'order_pickupstore': "Pickup Location",
            'order_returnstore': "Return Location",
            'order_customer': "Account Name",
            'order_car' : "Car Name"
        }

	def __init__(self, *args, **kwargs):
	    super(ReserveForm, self).__init__(*args, **kwargs)
	    self.helper = FormHelper()
	    self.helper.form_tag = True
	    self.helper.form_class = 'form-horizontal'
	    self.helper.label_class = 'col-sm-3'
	    self.helper.field_class = 'col-sm-9'
	    self.helper.add_input(Submit('submit', 'Confirm Checkout'))

class ReviewForm(forms.Form):
	content_type = forms.CharField(widget=forms.HiddenInput)
	object_id = forms.IntegerField(widget=forms.HiddenInput)
	content = forms.CharField(widget=forms.Textarea)




