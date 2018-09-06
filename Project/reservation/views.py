from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #return HttpResponse("<h2>Reservations page looking good</h2>")
    return render(request, 'reservation/index.html', {'title': 'Reservation1'})


