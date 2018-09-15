from django.shortcuts import render
from django.http import HttpResponse
from dataimport.testimport import importthedata
from dataimport.models import Customers
# Create your views here.
def index(request):
    if(request.GET.get('print_btn')):
        print('Button clicked')
        importthedata()
        a = Customers.objects.get(customer_id = 11011)
        print(a.customer_name)
    return HttpResponse(render(request, 'dataimport.html'))
