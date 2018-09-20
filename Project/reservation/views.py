from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


from .forms import *

from dataimport.models import *
from dataimport.testimport import importthedata
from django.urls import reverse


@login_required(login_url='/account/login')
def index(request,id):
	form = ReserveForm()
	obj = get_object_or_404(Cars, car_id=id)
	obj2 = Stores.objects.all()
	if request.method == "POST":
		form = ReserveForm(request.POST)
		if form.is_valid():
			Orders.objects.create(**form.cleaned_data)
			return HttpResponseRedirect(reverse('thanks_page'))
	context = {
		'form': form,
		'car' : obj,
		'store' : obj2
		}
	return render(request, 'reservation/test.html', context)

def details(request, id):
	obj = get_object_or_404(Cars, car_id=id)
	obj2 = Stores.objects.all()
	context = {
		'car' : obj,
		'store' : obj2
		}
	return render(request, 'reservation/car_details.html', context)



