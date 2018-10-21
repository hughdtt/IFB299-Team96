from django.shortcuts import render
from django.http import HttpResponse
from dataimport.models import Customers, User
from django.db.models import Q
from django.db import connection
from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404

# Create your views here.

def profile(request):
    user = request.user
    obj = get_object_or_404(Customers, user=user)
    
    return render(request, 'accounts/layout.html', {'custdata': obj})

