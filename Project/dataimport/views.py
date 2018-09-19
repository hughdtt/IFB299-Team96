from django.shortcuts import render
from django.http import HttpResponse
from dataimport.testimport import importthedata
from dataimport.models import Customers
# Create your views here.

#When the button is clicked, the csv data is imported.
#Refer to testimport.py for info
def index(request):
    if(request.GET.get('print_btn')):
        print('Button clicked')
        importthedata()
    return HttpResponse(render(request, 'dataimport.html'))
