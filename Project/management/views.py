from django.shortcuts import render

from django.views.generic import TemplateView


class ManagementPageView(TemplateView):
    template_name = 'management.html'
