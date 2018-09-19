from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import *
# Create your views here.

# Returns the loggedin.html view when the user is logged in. Replaced with going straight to the index currently.
def loggedin(request):
	
    return HttpResponse(render(request, 'loggedin.html'))

#Code which is used for creating accounts and verifying fields, before sending user to accountcreation.html
#Perhaps more documentation required here?
def create(request):
	form = CreateForm()
	if request.method == "POST":
		form = CreateForm(request.POST)
		if form.is_valid():
			Customers.objects.create(**form.cleaned_data)
	context = {
		'form': form,
		}
	return render(request, 'accountcreation.html', context)

class AccountCreationView(TemplateView):
    template_name = 'accountcreation.html'


