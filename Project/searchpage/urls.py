from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.search, name='search'),
    path('recommendation/', views.recommendation, name='recommendation'),
    path('results/',views.results, name='results'),


]
    
