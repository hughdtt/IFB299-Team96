
from django.http import HttpResponse
from searchpage.models import Table1
from django.shortcuts import render
from django.template.response import TemplateResponse


# Create your views here.

def index(request):
    #return HttpResponse("<h1>Seachpage title test")
    carData = Table1.objects.all()  
    return render(request, 'search/searchpage.html', {'Cars': carData})


