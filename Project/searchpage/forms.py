from django import forms
from dataimport.models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class RecommendForm(forms.ModelForm):
	class Meta:
		model = Cars
		fields = '__all__'
		widgets = {
			'car_id' : forms.RadioSelect(attrs={'type': 'radio'}),
			'car_make' : forms.RadioSelect(attrs={'type': 'radio'}),
			'car_model' : forms.RadioSelect(attrs={'type': 'radio'}),

		}

	def __init__(self, *args, **kwargs):
	    super(RecommendForm, self).__init__(*args, **kwargs)
	    self.helper = FormHelper()
	    self.helper.form_tag = True
	    self.helper.form_class = 'form-horizontal'
	    self.helper.label_class = 'col-sm-3'
	    self.helper.field_class = 'col-sm-9'
	    self.helper.add_input(Submit('submit', 'Confirm Checkout'))