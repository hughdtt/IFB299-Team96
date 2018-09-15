from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.
def loggedin(request):
	
    return HttpResponse(render(request, 'loggedin.html'))

class AccountCreationView(TemplateView):
    template_name = 'accountcreation.html'
