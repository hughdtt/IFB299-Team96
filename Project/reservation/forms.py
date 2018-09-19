from django import forms
from dataimport.models import *

class ReserveForm(forms.ModelForm):
	class Meta:
		model = Orders
		fields = '__all__'
		widgets = {
			'order_createdate' : forms.DateInput(attrs={'type': 'date'}),
			'order_pickupdate' : forms.DateInput(attrs={'type': 'date'}),
			'order_returndate' : forms.DateInput(attrs={'type': 'date'})

		}
		labels = {
            'order_pickupdate': "PickUp Date"
        }

