from django import forms
from crispy_forms.helper import FormHelper
from dataimport.models import *
from crispy_forms.layout import Submit


class ReserveForm(forms.ModelForm):
	class Meta:
		model = Orders
		fields = ('order_id', 'order_createdate', 'order_pickupdate', 'order_returndate',
			'order_pickupstore', 'order_returnstore', 'order_customer', 'order_car'
			)

