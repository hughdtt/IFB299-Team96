

#from searchpage.models import Table1
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.db import connection
from dataimport.models import Cars, Stores
from django.template.response import TemplateResponse
from .forms import *



# Create your views here.

def index(request):
    #return HttpResponse("<h1>Seachpage title test")
    carData = Cars.objects.all()  
    return render(request, 'search/searchpage.html', {'Cars': carData})

def recommendation(request):
    query = request.GET.get("query")
    querylist = Cars.objects.all()

    make = Cars.objects.values('car_make').order_by('car_make').distinct()
    model = Cars.objects.values('car_model').order_by('car_model').distinct()
    series = Cars.objects.values('car_series').order_by('car_series').distinct()
    year = Cars.objects.values('car_seriesyear').order_by('car_seriesyear').distinct()
    seats = Cars.objects.values('car_seatingcapacity').order_by('car_seatingcapacity').distinct()
    transmission = Cars.objects.values('car_standardtransmission').order_by('car_standardtransmission').distinct()
    drive = Cars.objects.values('car_drive').order_by('car_drive').distinct()
    priceMin = request.GET.get("priceMin")
    priceMax = request.GET.get("priceMax")

    context = {
        'searchedcars': querylist, 
        'carmake': make, 
        'carmodel': model, 
        'carseries': series, 
        'caryear': year, 
        'carseats': seats,
        'cartransmission': transmission, 
        'cardrive': drive
    }

    return render(request, 'search/recommendation.html', context)

def results(request):
    querylist = Cars.objects.all()
    context = {
        'searchedcars': querylist, 
    }
    return render(request, 'search/results.html', context)

def search(request):

    query = request.GET.get("query")
    querylist = Cars.objects.all()

    store = Stores.objects.values('store_name').order_by('store_name').distinct()
    make = Cars.objects.values('car_make').order_by('car_make').distinct()
    model = Cars.objects.values('car_model').order_by('car_model').distinct()
    series = Cars.objects.values('car_series').order_by('car_series').distinct()
    year = Cars.objects.values('car_seriesyear').order_by('car_seriesyear').distinct()
    seats = Cars.objects.values('car_seatingcapacity').order_by('car_seatingcapacity').distinct()
    transmission = Cars.objects.values('car_standardtransmission').order_by('car_standardtransmission').distinct()
    drive = Cars.objects.values('car_drive').order_by('car_drive').distinct()
    
    dropdownMake = request.GET.get("dropdownMake")
    dropdownModel = request.GET.get("dropdownModel")
    dropdownSeries = request.GET.get("dropdownSeries")
    dropdownYear = request.GET.get("dropdownYear")
    dropdownSeats = request.GET.get("dropdownSeats")
    dropdownTransmission = request.GET.get("dropdownTransmission")
    dropdownDrive = request.GET.get("dropdownDrive")

    if dropdownMake:
        querylist = querylist.filter(
            Q(car_make__icontains=dropdownMake)).distinct()
    
    if dropdownModel:
        querylist = querylist.filter(
            Q(car_model__icontains=dropdownModel)).distinct()
    
    if dropdownSeries:
        querylist = querylist.filter(
            Q(car_series__icontains=dropdownSeries)).distinct()

    if dropdownYear:
        querylist = querylist.filter(
            Q(car_seriesyear__icontains=dropdownYear)).distinct()
            
    if dropdownSeats:
        querylist = querylist.filter(
            Q(car_seatingcapacity__icontains=dropdownSeats)).distinct()
    
    if dropdownTransmission:
            querylist = querylist.filter(
                Q(car_standardtransmission__icontains=dropdownTransmission)).distinct()

    if dropdownDrive:
            querylist = querylist.filter(
                Q(car_drive__icontains=dropdownDrive)).distinct()            

    if query:
        querylist = querylist.filter(
            Q(car_id__icontains=query) |
            Q(car_make__icontains=query) |
            Q(car_model__icontains=query) |
            Q(car_series__icontains=query) |
            Q(car_seriesyear__icontains=query) |
            Q(car_pricenew__icontains=query) |          
            Q(car_enginesize__icontains=query) |
            Q(car_fuelsystem__icontains=query) |
            Q(car_tankcapacity__icontains=query) |
            Q(car_power__icontains=query) |
            Q(car_seatingcapacity__icontains=query) |
            Q(car_standardtransmission__icontains=query) |
            Q(car_bodytype__icontains=query) |
            Q(car_drive__icontains=query) |
            Q(car_wheelbase__icontains=query)     
        ).distinct()
    return render(request, 'search/searchpage.html', {'searchedcars': querylist, 'carstore': store, 'carmake': make, 'carmodel': model, 'carseries': series, 'caryear': year, 'carseats': seats,
    'cartransmission': transmission, 'cardrive': drive})


