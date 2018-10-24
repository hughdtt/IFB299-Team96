from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from collections import OrderedDict
from dataimport.models import Orders,Stores
from django.db import models
from datetime import date
from .fusioncharts import FusionCharts
import calendar
from django.contrib.auth.mixins import LoginRequiredMixin



class ManagementPageView(LoginRequiredMixin, TemplateView):
    login_url = '/account/login'
    template_name = 'management.html'
    

def analytics(request):
    
    stores = Stores.objects.values('store_name').order_by('store_name').distinct().values_list('store_name',flat=True)
    years = Orders.objects.dates('order_createdate','year',order='DESC').distinct()
    granularity = ["All","By Year","By Month"]
    months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    # Chart data is passed to the `dataSource` parameter, as dictionary in the form of key-value pairs.
    dataSource = OrderedDict()
    getData = request.GET
    storeGet = getData.get("Store",default="All Stores")
    gGet = getData.get("g",default="All")
    yearGet = getData.get("year",default="2005")
    monthGet = getData.get("month",default="1")

    # The `chartConfig` dict contains key-value pairs data for chart attribute
    chartConfig = OrderedDict()
    chartConfig["caption"] = "Customer Orders By Year"
    chartConfig["subCaption"] = "Subcaption"
    chartConfig["xAxisName"] = "Year"
    chartConfig["yAxisName"] = "Orders"
    chartConfig["labelDisplay"] = "rotate"
    chartConfig["numberSuffix"] = ""
    chartConfig["theme"] = "fusion"

    # The `chartData` dict contains key-value pairs data
    chartData = OrderedDict()
    if storeGet == "All Stores":
        orderFiltered = Orders.objects
    else:
        storeToAnalyse = Stores.objects.get(store_name=storeGet)
        orderFiltered = Orders.objects.filter(order_pickupstore=storeToAnalyse)
    #TODO: FIX THIS
    years2 = years
    monthNumber = 1
    if gGet != "All":
        years2 = years.filter(order_createdate__range=(date(int(yearGet),1,1),date(int(yearGet),12,31)))
    
    if gGet == "By Month":
        for i in range(1,12):
            if(monthGet == months[i]):
                monthNumber = i

    
    for x in years2:
        if gGet == "By Year":
            for mth in range(1,13):
                chartData[str(months[mth-1])] = orderFiltered.filter(order_createdate__range=(date(x.year,mth,1),date(x.year,mth,calendar.monthrange(x.year,mth)[1]))).count()
        elif gGet == "By Month":
            
            for day in range(1,calendar.monthrange(x.year,monthNumber)[1]):
                chartData[str(day) + "-" + monthGet] = orderFiltered.filter(order_createdate=(date(x.year,monthNumber,day))).count()
        else:
            chartData[str(x.year)] = orderFiltered.filter(order_createdate__range=(date(x.year,1,1),date(x.year,12,31))).count()

        
    '''
    chartData["2005"] = Orders.objects.filter(order_createdate__range=(date(2005,1,1),date(2005,12,31))).count()
    chartData["2006"] = Orders.objects.filter(order_createdate__range=(date(2006,1,1),date(2006,12,31))).count()
    chartData["2007"] = Orders.objects.filter(order_createdate__range=(date(2007,1,1),date(2007,12,31))).count()
    '''

    dataSource["chart"] = chartConfig
    dataSource["data"] = []
    
    # Convert the data in the `chartData` array into a format that can be consumed by FusionCharts. 
    # The data for the chart should be in an array wherein each element of the array is a JSON object
    # having the `label` and `value` as keys.

    # Iterate through the data in `chartData` and insert in to the `dataSource['data']` list.
    for key, value in chartData.items():
        data = {}
        data["label"] = key
        data["value"] = value
        dataSource["data"].append(data)

    # Create an object for the column 2D chart using the FusionCharts class constructor
    # The chart data is passed to the `dataSource` parameter.
    column2D = FusionCharts("column2d", "ex1" , "600", "400", "data-chart", "json", dataSource)
    #years = Orders.objects.values('order_createdate').order_by('order_createdate').distinct()
    years = list(years)
    months = list(months)
    stores = list(stores)
    granularity = list(granularity)
    #years[1] = "<delete" + str(years[1])
    #print(years[1])
    #error()
    i = 0
    for yr in years:
        print(str(yearGet) == str(yr.year))
        print(str(yearGet))
        print(str(yr.year))
        if(str(yearGet) == str(yr.year)):
            years[i] = "selected >" + str(years[i].year)
        else:
            years[i] = ">" + str(years[i].year)
        print(years[i])
        i = i + 1

    i = 0
    for mth in months:
        if(monthGet == str(mth)):
            months[i] = "selected >" + str(months[i])
        else:
            months[i] = ">" + str(months[i])
        i = i + 1
    i = 0
    for gr in granularity:
        if(gGet == granularity[i]):
            granularity[i] = "selected >" + granularity[i]
        else:
            granularity[i] = ">" + granularity[i]
        i = i + 1
    i = 0
    for store in stores:
        if(storeGet == store):
            stores[i] = "selected >" + str(stores[i])
        else:
            stores[i] = ">" + str(stores[i])
        i = i + 1
        
    return  render(request, 'analytics.html', {'output' : column2D.render(), 'years' : years, 'stores' : stores, 'granularity' : granularity, 'months' : months})

def store(request):
    getData = request.GET
    idGet = int(getData.get("id",default="0"))
    storeGet = int(getData.get("Store",default="1"))
    stores = Stores.objects.values('store_id','store_name').order_by('store_name').distinct()
    if(idGet > 0):
        order_to_modify = Orders.objects.get(order_id=idGet)
        status = order_to_modify.order_status
        if(status == 1):
            status = 2
        else:
            status = 3
            order_to_modify.order_car.car_in_us = 0
            order_to_modify.order_car.save()
        order_to_modify.order_status = status
        order_to_modify.save()
    topickup = Orders.objects.filter(order_pickupstore=storeGet).filter(order_status=1)
    todropoff = Orders.objects.filter(order_returnstore=storeGet).filter(order_status=2)
    print(topickup)
    print(todropoff)
    return HttpResponse(render(request, 'store.html',{'stores' : stores, 'selectedStore' : storeGet, 'topickup' : topickup, 'todropoff' : todropoff}))
