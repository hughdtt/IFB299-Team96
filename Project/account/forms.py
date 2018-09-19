from django import forms
from dataimport.models import *

class CreateForm(forms.ModelForm):
	class Meta:
		model = Customers 
		fields = '__all__'
		