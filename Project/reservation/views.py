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

	#order_id = request.Orders.order_id
	car_name = id
	account_name = request.user
	initial_data = {
		#"order_id" : order_id,
		"order_car" : car_name,
		"order_customer" : account_name,
		"order_status" : 1,
	}

	if request.method == "POST":
		form = ReserveForm(request.POST or None, initial=initial_data)
		print('something')
		if form.is_valid():
			order_id = form.cleaned_data.get("order_id")
			pickup_data = form.cleaned_data.get("order_pickupdate")
			return_data = form.cleaned_data.get("order_returndate")
			pickupstore_data = form.cleaned_data.get("order_pickupstore")
			returnstore_data = form.cleaned_data.get("order_returnstore")
			account_name = form.cleaned_data.get("order_customer")
			car_data = form.cleaned_data.get("order_car")
			new_order = Orders.objects.get_or_create(
									order_id = order_id,
									order_status = 1,
									order_pickupdate = pickup_data,
									order_returndate = return_data,
									order_pickupstore = pickupstore_data,
									order_returnstore = returnstore_data,
									order_customer = account_name,
									order_car = car_data,
								)
			print('saved')
			car_obj = car_data
			car_obj.car_in_use = 1
			car_obj.save()
			return HttpResponseRedirect(reverse('thanks_page'))
		else:
			form = ReserveForm(initial=initial_data)
	context = {
		'form': form,
		'car' : obj,
		'store' : obj2
		}
	return render(request, 'reservation/test.html', context)

def details(request, id):
	review_form = ReviewForm()
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
	#Calls the ReviewForm from forms.py applying initial data from above
	review_form = ReviewForm(request.POST, initial=initial_data)
	if review_form.is_valid():
		c_type = review_form.cleaned_data.get("content_type")  # Get Content_type
		content_type = ContentType.objects.get(model=c_type) # Get Content_type
		obj_id = review_form.cleaned_data.get("object_id") # Get Object ID
		content_data = review_form.cleaned_data.get("content") # Get the Content / Review Message
		new_review, created = Reviews.objects.get_or_create(
									author = request.user,
									content_type = content_type,
									object_id = obj_id,
									content = content_data
								)
		#Creates the new message and saves it
		print('success')
	else:
		#if the form is not valid, it will just initiate the clean form again
		review_form = ReviewForm(initial=initial_data)
		print('no')

	context = {
		'car' : instance,
		'review' : review,
		'review_form' : review_form,
		}

	return render(request, 'reservation/car_details.html', context)



