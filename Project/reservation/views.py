from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import CreateView

from .models import *
from .forms import *

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

def thanks(request):
	return render(request, 'reservation/thanks.html')

class TesterCreate(CreateView):
	model = Reservation
	form_class = ReserveForm
	template_name = 'reservation/reservation_form.html'



