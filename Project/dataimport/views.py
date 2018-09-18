from django.shortcuts import render
from django.http import HttpResponse
from dataimport.testimport import importthedata
from dataimport.models import Customers
# Create your views here.
def index(request):
    if(request.GET.get('print_btn')):
        print('Button clicked')
        importthedata()
    return HttpResponse(render(request, 'dataimport.html'))
