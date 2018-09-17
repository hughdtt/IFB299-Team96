from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView


from .models import *
from .forms import *

from dataimport.models import *
from dataimport.testimport import importthedata

def index(request, id):
	obj = get_object_or_404(Cars, car_id=id)
	obj2 = Stores.objects.all()
	context = {
		'car' : obj,
		'store' : obj2
		}
	return render(request, 'reservation/index.html', context)

def details(request, id):
	obj = Cars.objects.get(car_id = id )
	obj2 = Stores.objects.all()
	context = {
		'car' : obj,
		'store' : obj2
		}
	return render(request, 'reservation/car_details.html', context)


class ReserveCreate(CreateView):
	model = Reservation
	form_class = ReserveForm
	template_name = 'reservation/reservation_form.html'

	def get_absolute_url(self):
		return reverse('reservation:reservation_form')


