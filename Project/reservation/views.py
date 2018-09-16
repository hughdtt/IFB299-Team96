from django.shortcuts import render
from django.shortcuts import render

from .forms import StoreForm
from dataimport.models import *
from dataimport.testimport import importthedata

def index(request):
	obj = Cars.objects.get(car_id = 15400 )
	obj2 = Stores.objects.all()
	context = {
		'car' : obj,
		'store' : obj2
		}
	return render(request, 'reservation/index.html', context)






