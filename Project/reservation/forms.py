from django import forms
from crispy_forms.helper import FormHelper
from dataimport.models import *
from crispy_forms.layout import Submit
from .models import *

class ReserveForm(forms.ModelForm):
	class Meta:
		model = Reservation
		fields = ('name', 'store_loc', 'pickup_dte', 'return_dte')

	def clean_title(self, *args, **kwargs):
		name = self.cleaned_data.get("name")
		if not "admin" in title:
			raise forms.ValidationError("This is not a valid title")
		return name

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Reserve Car'))
