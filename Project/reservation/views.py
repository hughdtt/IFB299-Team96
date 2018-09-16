from django.shortcuts import render
from django.template.response import TemplateResponse

from .forms import NameForm
from dataimport.models import *
from dataimport.testimport import importthedata

def index(request):
	data = Cars.objects.get(car_make = "HONDA")
	print(data.car_make)
	return TemplateResponse(request, 'reservation/index.html', {"data": data})






