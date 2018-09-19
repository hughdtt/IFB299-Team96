from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#Used for the home page
def index(request):
	
    return HttpResponse(render(request, 'index.html'))