

from searchpage.models import Table1
from django.shortcuts import render
from django.db.models import Q


# Create your views here.
"""
def index(request):
    #return HttpResponse("<h1>Seachpage title test")
    carData = Table1.objects.all()  
    return render(request, 'search/searchpage.html', {'Cars': carData})
"""

def search(request):
    query = request.GET.get("query")
    querylist = Table1.objects.all()
    if query:
        querylist = querylist.filter(
            Q(car_id__icontains=query) |
            Q(car_makename__icontains=query) |
            Q(car_model__icontains=query) |
            Q(car_series__icontains=query) |
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
    return render(request, 'search/searchpage.html', {'searchedcars': querylist})
