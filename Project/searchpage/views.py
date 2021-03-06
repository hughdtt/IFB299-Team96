
#from searchpage.models import Table1
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
from django.db import connection
from dataimport.models import Cars, Stores
from django.template.response import TemplateResponse



# Create your views here.

def index(request):
    #return HttpResponse("<h1>Seachpage title test")
    carData = Cars.objects.all()  
    return render(request, 'search/searchpage.html', {'Cars': carData})

def recommendation(request):
    querylist = Cars.objects.all().exclude(car_make="NULL").order_by('car_make')
    querylist = querylist.filter(car_in_use = 0)
    dropdownPrice = request.GET.get("dropdownPrice")
    dropdownLength = request.GET.get("dropdownLength")
    print(dropdownPrice)
    print(dropdownLength)
    if dropdownPrice == 'expensive':
        print(dropdownPrice)
        if dropdownLength == 'less':
            querylist = querylist.filter(
                Q(car_make__icontains='Alfa Romeo') |
                Q(car_make__icontains='Audi') |
                Q(car_make__icontains='BMW') |
                Q(car_make__icontains='Chrysler')).distinct()
        else:
            querylist = querylist.filter(
                Q(car_make__icontains='Land Rover') |
                Q(car_make__icontains='Mercedes-Benz') |
                Q(car_make__icontains='Volvo')).distinct()
    if dropdownPrice == 'cheap':
        print(dropdownPrice)
        if dropdownLength == 'less':
            querylist = querylist.filter(
                Q(car_make__icontains='Euno') |
                Q(car_make__icontains='Honda') |
                Q(car_make__icontains='Mazda') |
                Q(car_make__icontains='Mitsubishi') |
                Q(car_make__icontains='Nissan')).distinct()
        else:
            querylist = querylist.filter(
                Q(car_make__icontains='Peugot') |
                Q(car_make__icontains='Renault') |
                Q(car_make__icontains='Saab') |
                Q(car_make__icontains='Toyota') |
                Q(car_make__icontains='Volkswagen')).distinct()  


    context = {
    'searchedcars': querylist,
    }

    return render(request, 'search/recommendation.html', context)

def search(request):  
    query = request.GET.get("query")
    querylist = Cars.objects.all().exclude(car_make="NULL")
    querylist = querylist.filter(car_in_use = 0)

    make = Cars.objects.values('car_make').exclude(car_make="NULL").order_by('car_make').distinct()
    model = Cars.objects.values('car_model').exclude(car_model="NULL").order_by('car_model').distinct()
    series = Cars.objects.values('car_series').exclude(car_series="NULL").order_by('car_series').distinct()
    year = Cars.objects.values('car_seriesyear').order_by('car_seriesyear').distinct()
    seats = Cars.objects.values('car_seatingcapacity').order_by('car_seatingcapacity').distinct()
    transmission = Cars.objects.values('car_standardtransmission').exclude(car_standardtransmission="NULL").order_by('car_standardtransmission').distinct()
    drive = Cars.objects.values('car_drive').exclude(car_drive="NULL").order_by('car_drive').distinct()
    
    dropdownMake = request.GET.get("dropdownMake")
    dropdownModel = request.GET.get("dropdownModel")
    dropdownSeries = request.GET.get("dropdownSeries")
    dropdownYear = request.GET.get("dropdownYear")
    dropdownSeats = request.GET.get("dropdownSeats")
    dropdownTransmission = request.GET.get("dropdownTransmission")
    dropdownDrive = request.GET.get("dropdownDrive")

    if dropdownMake:
        print(dropdownMake)
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

    return render(request, 'search/searchpage.html', {'searchedcars': querylist, 'carmake': make, 'carmodel': model, 'carseries': series, 'caryear': year, 'carseats': seats,
    'cartransmission': transmission, 'cardrive': drive, 'query': query})


