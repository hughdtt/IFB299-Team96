from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from .forms import *
from dataimport.models import Customers
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.urls import reverse
# Create your views here.

# Returns the loggedin.html view when the user is logged in. Replaced with going straight to the index currently.
def loggedin(request):
	
    return HttpResponse(render(request, 'loggedin.html'))

#Code which is used for creating accounts and verifying fields, before sending user to accountcreation.html
#Perhaps more documentation required here?
            

def create(request):
	user_form = UserCreationForm()
	profile_form = ProfileForm()
	if request.method == 'POST':
		user_form = UserCreationForm(request.POST or None)
		profile_form = ProfileForm(request.POST or None)
		if user_form.is_valid() or profile_form.is_valid():
			user = user_form.save()
			user.refresh_from_db()  # This will load the Profile created by the Signal
			customers = Customers.objects.get(user=user)
			profile_form = ProfileForm(request.POST or None, instance=customers)  # Reload the profile form with the profile instance
			profile_form.full_clean()  # Manually clean the form this time. It is implicitly called by "is_valid()" method
			profile_form.save()  # Gracefully save the form
			raw_password = user_form.cleaned_data.get('password1')
			user = authenticate(username=user.username, password=raw_password)
			login(request, user)
			return HttpResponseRedirect(reverse('thanks_page'))

		else:
			user_form = UserCreationForm()
			profile_form = ProfileForm()

	context = {
	'user_form': user_form,
	'profile_form' : profile_form,
	}

	return render(request, 'accountcreation.html', context)

# mb for profile page?
def create_customer(request):
	if request.method == 'POST':

		username = request.user
		print(username)

		initial_data = {
		'user' : username
		}

		profile_form = ProfileForm(request.POST or None, initial = initial_data)

		if profile_form.is_valid():  # Reload the profile form with the profile instance
			profile_form.full_clean()  # Manually clean the form this time. It is implicitly called by "is_valid()" method
			profile_form.save()  # Gracefully save the form
			return HttpResponseRedirect(reverse('thanks_page'))

	else:
		profile_form = ProfileForm()

	context = {
	'profile_form' : profile_form
	}

	return render(request, 'accountcreationstep2.html', context)