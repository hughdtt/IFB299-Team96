from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
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
		user_form = UserCreationForm(request.POST)
		profile_form = ProfileForm(request.POST)
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.refresh_from_db()  # This will load the Profile created by the Signal
			profile_form = ProfileForm(request.POST, instance=user.customer)  # Reload the profile form with the profile instance
			profile_form.full_clean()  # Manually clean the form this time. It is implicitly called by "is_valid()" method
			profile_form.save()
			user.save() # Gracefully save the form
			raw_password = user_form.cleaned_data.get('password1')
			user = authenticate(username=user.username, password=raw_password)
			login(request, user)
			return redirect('home')
		else:
			user_form = UserCreationForm()
			profile_form = ProfileForm()

	context = {
	'user_form': user_form,
	'profile_form': profile_form
	}

	return render(request, 'accountcreation.html', context)
            


