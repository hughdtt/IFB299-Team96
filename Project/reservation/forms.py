from django import forms
from crispy_forms.helper import FormHelper
from dataimport.models import *
from crispy_forms.layout import Submit
from .models import *

class ReserveForm(forms.ModelForm):
	class Meta:
		model = Reservation
		fields = ('name', 'store_loc', 'pickup_dte', 'return_dte')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Save person'))
