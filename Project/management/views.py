from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from collections import OrderedDict
from dataimport.models import Orders,Stores
from django.db import models
from datetime import date
from .fusioncharts import FusionCharts
import calendar

class ManagementPageView(TemplateView):
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
    if gGet != "All":
        years2 = years.filter(order_createdate__range=(date(int(yearGet),1,1),date(int(yearGet),12,31)))
    

    
    for x in years2:
        if gGet == "By Year":
            for mth in range(1,12):
                chartData[str(months[mth])] = orderFiltered.filter(order_createdate__range=(date(x.year,mth,1),date(x.year,mth,calendar.monthrange(x.year,mth)[1]))).count()
        else:
            chartData[str(x.year)] = orderFiltered.filter(order_createdate__range=(date(x.year,1,1),date(x.year,12,31))).count()
        print(x.year)

        
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
    for specificStore in stores:
        print("DELET THIS")
    return  render(request, 'analytics.html', {'output' : column2D.render(), 'years' : years, 'stores' : stores, 'granularity' : granularity, 'months' : months})