from django import forms

class RecommendForm(forms.Form):
	family = forms.BooleanField(required=False)
	adventure = forms.BooleanField(required=False)
	trade = forms.BooleanField(required=False)
	prestige = forms.BooleanField(required=False)
	eco = forms.BooleanField(required=False)
	value = forms.BooleanField(required=False)
	performance = forms.BooleanField(required=False)
	safety = forms.BooleanField(required=False)
	comfort = forms.BooleanField(required=False)
	space = forms.BooleanField(required=False)