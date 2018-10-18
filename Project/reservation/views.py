from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
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
		else:
			form = ReserveForm()
	context = {
		'form': form,
		'car' : obj,
		'store' : obj2
		}
	return render(request, 'reservation/test.html', context)

def details(request, id):
	#Calls Specific Car details
	instance = get_object_or_404(Cars, car_id=id)

	#Foreign Key for comments
	content_type = ContentType.objects.get_for_model(Cars)
	object_id = id
	review = Reviews.objects.filter(content_type=content_type, object_id=object_id)	

	#Form stuff - Initial data
	initial_data = {
		"content_type": content_type,
		"object_id": object_id,

	}

	review_form = ReviewForm(request.POST or None, initial=initial_data)
	if review_form.is_valid():
		c_type = review_form.cleaned_data.get("content_type")
		content_type = ContentType.objects.get(model=c_type)
		obj_id = review_form.cleaned_data.get("object_id")
		content_data = review_form.cleaned_data.get("content")
		new_review, created = Reviews.objects.get_or_create(
									author = request.user,
									content_type = content_type,
									object_id = obj_id,
									content = content_data
								)

	context = {
		'car' : instance,
		'review' : review,
		'review_form' : review_form,
		}

	return render(request, 'reservation/car_details.html', context)



