from django.shortcuts import render
from django.views.generic import TemplateView

class AccountCreationView(TemplateView):
    template_name = 'accountcreation.html'
