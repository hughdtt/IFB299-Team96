from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from collections import OrderedDict
from dataimport.models import Orders
from django.db import models
from datetime import date
from .fusioncharts import FusionCharts

class ManagementPageView(TemplateView):
    template_name = 'management.html'

def analytics(request):

    # Chart data is passed to the `dataSource` parameter, as dictionary in the form of key-value pairs.
    dataSource = OrderedDict()

    # The `chartConfig` dict contains key-value pairs data for chart attribute
    chartConfig = OrderedDict()
    chartConfig["caption"] = "Customer Orders By Year"
    chartConfig["subCaption"] = "Subcaption"
    chartConfig["xAxisName"] = "Year"
    chartConfig["yAxisName"] = "Orders"
    chartConfig["numberSuffix"] = ""
    chartConfig["theme"] = "fusion"

    # The `chartData` dict contains key-value pairs data
    chartData = OrderedDict()
    chartData["2005"] = Orders.objects.filter(order_createdate__range=(date(2005,1,1),date(2005,12,31))).count()
    chartData["2006"] = Orders.objects.filter(order_createdate__range=(date(2006,1,1),date(2006,12,31))).count()
    chartData["2007"] = Orders.objects.filter(order_createdate__range=(date(2007,1,1),date(2007,12,31))).count()


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

    return  render(request, 'analytics.html', {'output' : column2D.render()})