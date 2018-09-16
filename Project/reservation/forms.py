from django import forms
from dataimport.models import *

class StoreForm(forms.Form):
    class Meta:
    	model = Stores
    	fields = [
    		'name'
    	]